from structures.em_t_panel import EMTPanel
from structures.em_info_panel import EMInfoPanel
from structures.third_party_panel import ThirdPartyPanel
from services.logger import Logger
from utils.db_utils import safe_int

from structures.efs_panel_enums import (
    EfsPanelModel, EfsPanelType, EfsPanelSize,
    EMTPanelModel, EMTPanelSize,
    EMInfoPanelModel, EMInfoPanelSize,
    ThirdPartyPanelType, ThirdPartyPanelAspectRatio
)

THIRD_PARTY_ID_OFFSET = 1000

class EthernetPanelsMapper:

    _EMT_MODEL = {
        EfsPanelModel.ModelT1:    EMTPanelModel.T1,
        EfsPanelModel.ModelT2:    EMTPanelModel.T2,
        EfsPanelModel.ModelTLite: EMTPanelModel.TLite,
        EfsPanelModel.ModelT3:    EMTPanelModel.T3,
        EfsPanelModel.ModelT4:    EMTPanelModel.T4,
    }

    _EMT_SIZE = {
        EfsPanelSize.Size50x40: EMTPanelSize.Size50x40,
        EfsPanelSize.Size30x28: EMTPanelSize.Size30x28,
        EfsPanelSize.Size30x24: EMTPanelSize.Size30x24,
        EfsPanelSize.Size48x48: EMTPanelSize.Size48x48,
        EfsPanelSize.Size40x40: EMTPanelSize.Size40x40,
        EfsPanelSize.Size32x32: EMTPanelSize.Size32x32,
    }

    _EMI_MODEL = {
        EfsPanelModel.ModelEMLiveBoard: EMInfoPanelModel.EM1,
    }

    _EMI_SIZE = {
        EfsPanelSize.Size96x64:   EMInfoPanelSize.Size96x64,
        EfsPanelSize.Size112x72:  EMInfoPanelSize.Size112x72,
        EfsPanelSize.Size192x96:  EMInfoPanelSize.Size192x96,
        EfsPanelSize.Size64x64:   EMInfoPanelSize.Size64x64,
        EfsPanelSize.Size192x128: EMInfoPanelSize.Size192x128,
        EfsPanelSize.Size360x150: EMInfoPanelSize.Size360x150,
        EfsPanelSize.Size384x128: EMInfoPanelSize.Size384x128,
        EfsPanelSize.Size256x128: EMInfoPanelSize.Size256x128,
        EfsPanelSize.Size384x64:  EMInfoPanelSize.Size384x64,
        EfsPanelSize.Size624x312: EMInfoPanelSize.Size624x312,
        EfsPanelSize.Size312x208: EMInfoPanelSize.Size312x208,
        EfsPanelSize.Size768x512: EMInfoPanelSize.Size768x512,
    }

    _TP_TYPE = {
        EfsPanelType.TrackSidePanel: ThirdPartyPanelType.TrackSide,
        EfsPanelType.PitlanePanel:   ThirdPartyPanelType.TrackSide,
        EfsPanelType.InfoPanel:      ThirdPartyPanelType.Info,
    }

    _TP_ASPECT_RATIO = {
        EfsPanelSize.Size192x96:  ThirdPartyPanelAspectRatio.Ratio2_1,
        EfsPanelSize.Size192x128: ThirdPartyPanelAspectRatio.Ratio3_2,
    }


    def _read_(self, old_cursor) -> tuple[list[EMTPanel], list[EMInfoPanel], list[ThirdPartyPanel]]:

        old_cursor.execute("SELECT * FROM t_ethernet_panels")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_ethernet_panels")

        t_panels       = []
        info_panels    = []
        third_party    = []

        for row in rows:
            if row["ID"] >= THIRD_PARTY_ID_OFFSET:
                third_party.append(self._map_row_to_third_party(row))
            elif safe_int(row["Type"]) == 2:
                info_panels.append(self._map_row_to_info_panel(row))
            else:
                t_panels.append(self._map_row_to_t_panel(row))

        Logger.info(f"  -> {len(t_panels)} t_panels (trackside/pitlane)")
        Logger.info(f"  -> {len(info_panels)} info_panels")
        Logger.info(f"  -> {len(third_party)} third_party_panels")

        return t_panels, info_panels, third_party

    def _map_row_to_t_panel(self, row) -> EMTPanel:

        p = EMTPanel()

        p.id                     = row["ID"]
        p.active                 = row["Active"]
        p.model                  = self._EMT_MODEL.get(safe_int(row["Model"]), 1)
        p.size                   = self._EMT_SIZE.get(safe_int(row["Size"]), 1)
        p.name                   = row["Name"]
        p.address                = row["Address"]
        p.port                   = row["Port"]
        p.upload_address         = row["UploadAddress"]
        p.upload_port            = row["UploadPort"]
        p.marshal_remote_control = row["HasMarshalRemoteControl"]

        return p

    def _map_row_to_info_panel(self, row) -> EMInfoPanel:

        p = EMInfoPanel()

        p.id      = row["ID"]
        p.active  = row["Active"]
        p.model   = self._EMI_MODEL.get(safe_int(row["Model"]), 1)
        p.size    = self._EMI_SIZE.get(safe_int(row["Size"]), 1)
        p.name    = row["Name"]
        p.address = row["Address"]
        p.port    = row["Port"]

        return p

    def _map_row_to_third_party(self, row) -> ThirdPartyPanel:

        p = ThirdPartyPanel()

        p.id         = row["ID"] - THIRD_PARTY_ID_OFFSET
        p.active     = row["Active"]
        p.name       = row["Name"]
        p.panel_type = self._TP_TYPE.get(safe_int(row["Type"]), 1)
        p.aspect_ratio = self._TP_ASPECT_RATIO.get(safe_int(row["Size"]), 0)

        return p

    def _write_(self, new_cursor,
                t_panels: list[EMTPanel],
                info_panels: list[EMInfoPanel],
                third_party: list[ThirdPartyPanel]):

        new_cursor.execute("DELETE FROM t_em_t_panels")
        sql_t = """
            INSERT INTO t_em_t_panels (
                ID, Active, Model, Size, Name,
                Address, Port, UploadAddress, UploadPort, MarshalRemoteControl
            ) VALUES (?,?,?,?,?,?,?,?,?,?)
        """
        new_cursor.executemany(sql_t, [p.to_db_tuple() for p in t_panels])
        Logger.info(f"Written {len(t_panels)} records to t_em_t_panels")

        new_cursor.execute("DELETE FROM t_em_info_panels")
        sql_info = """
            INSERT INTO t_em_info_panels (
                ID, Active, Model, Size, Name, Address, Port
            ) VALUES (?,?,?,?,?,?,?)
        """
        new_cursor.executemany(sql_info, [p.to_db_tuple() for p in info_panels])
        Logger.info(f"Written {len(info_panels)} records to t_em_info_panels")

        new_cursor.execute("DELETE FROM t_third_party_panels")
        sql_tp = """
            INSERT INTO t_third_party_panels (
                ID, Active, Name, PanelType, AspectRatio
            ) VALUES (?,?,?,?,?)
        """
        new_cursor.executemany(sql_tp, [p.to_db_tuple() for p in third_party])
        Logger.info(f"Written {len(third_party)} records to t_third_party_panels")