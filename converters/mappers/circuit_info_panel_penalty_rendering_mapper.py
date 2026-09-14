from structures.circuit_info_panel_penalty_rendering import CircuitInfoPanelPenaltyRendering
from utils.flag_converter import convert_penalty_flag
from services.logger import Logger
from utils.db_utils import safe_int


class CircuitInfoPanelPenaltyRenderingMapper:

    def _read_(self, old_cursor) -> list[CircuitInfoPanelPenaltyRendering]:

        old_cursor.execute("SELECT * FROM t_info_panel_penalty_rendering")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_info_panel_penalty_rendering")

        result = []

        for row in rows:
            old_penalty = safe_int(row["Penalty"])
            new_penalty = convert_penalty_flag(old_penalty)

            if new_penalty is None:
                Logger.warn(f"No mapping for penalty flag {old_penalty}, skipping")
                continue

            r = CircuitInfoPanelPenaltyRendering()
            r.id               = row["FlagId"]
            r.circuit_id       = row["MapId"]
            r.penalty          = int(new_penalty)
            r.text_color       = row["TextColor"]
            r.background_color = row["BackgroundColor"]
            r.flashing_mode    = row["FlashingMode"]

            result.append(r)

        Logger.info(f"Composed {len(result)} penalty rendering records")
        return result

    def _write_(self, new_cursor, records: list[CircuitInfoPanelPenaltyRendering]):

        new_cursor.execute("DELETE FROM t_circuit_info_panel_penalty_rendering")

        sql = """
            INSERT INTO t_circuit_info_panel_penalty_rendering (
                ID, CircuitID, Penalty, TextColor, BackgroundColor, FlashingMode
            ) VALUES (?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [r.to_db_tuple() for r in records])
        Logger.ok(f"Written {len(records)} records to t_circuit_info_panel_penalty_rendering")