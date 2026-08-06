from structures.circuit import Circuit
from services.logger import Logger

class CircuitsMapper:

    def _read_(self, old_cursor) -> list[Circuit]:

        old_cursor.execute("SELECT * FROM t_maps")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_maps")

        circuits = [self._map_row_(row) for row in rows]

        #for c in circuits:
        #    print(c)

        return circuits

    def _map_row_(self, row) -> Circuit:

        c = Circuit()

        c.id                                        = row["ID"]
        c.circuit_number                            = row["PanelGroup"]
        c.name                                      = row["Name"]
        c.active                                    = row["Active"]
        c.map_file_name                             = row["MapFile"]
        c.map_file_md5                              = row["MapFileMD5"]
        c.sm_map_file_name                          = row["SMMapFile"]
        c.sm_map_file_md5                           = row["SMMapFileMD5"]
        c.sm_map_file_hash                          = row["MapHash"]
        c.flag_set                                  = row["FlagSet"]
        c.password                                  = row["Password"]
        c.aks_timing_server_id                      = row["AksTimingServerId"]

        if row["TracksidePanelsBrightness"] == '-1':  c.track_side_panel_brightness = 0
        else:                                         c.track_side_panel_brightness = row["TracksidePanelsBrightness"]
        if row["InfoPanelsBrightness"] == '-1':       c.info_panel_brightness = 0
        else:                                         c.info_panel_brightness = row["InfoPanelsBrightness"]
        if row["PitlanePanelsBrightness"] == '-1':    c.pitlane_panel_brightness = 0
        else:                                         c.pitlane_panel_brightness = row["PitlanePanelsBrightness"]

        c.tla_blue_flag_rendering                   = row["CustomBlueFlagRendering"]
        c.info_panel_rendering                      = row["InfoPanelRendering"]
        c.timing_master_role                        = row["CircuitTimingMasterRole"]
        c.use_yellow_flag_for_fcy_enabled           = row["UseYellowFlagForFCYEnabled"]
        c.track_panels_blacks_display_mode          = row["TrackPanelsBlacksDisplayMode"]
        c.use_three_stripes_yellow_red_flag_enabled = row["UseThreeStripesYellowRedFlagEnabled"]
        c.white_button_mode                         = row["MarshalConsoleWhiteButtonMode"]
        c.car_blue_flag_follow_on_panels            = row["AutoBlueFlagFollowOnPanels"]
        c.car_blue_flag_show                        = row["AutoBlueFlagVisualizationMode"]
        
        raw = row["StartingLightsControlUnitId"]
        if raw and str(raw).strip():
            c.starting_lights_control_unit_id = str(raw).split(",")[0].strip()
        else:
            c.starting_lights_control_unit_id = ""

        settings = 0
        if row["MarshalConsoleRedAndSCEnabled"] == '1':                        settings |= 0x001  # RedAndSCEnabled
        if row["MarshalConsoleSecondFrequencyEnabled"] == '1':                 settings |= 0x002  # SecondFrequencyEnabled
        if row["MarshalConsolePushEnabled"] == '1':                            settings |= 0x004  # PushEnabled
        if row["MarshalConsoleBlueEnabled"] == '1':                            settings |= 0x008  # BlueEnabled
        if row["MarshalConsole3FlashesBlueEnabled"] == '1':                    settings |= 0x010  # ThreeFlashesBlueEnabled
        if row["MarshalConsoleBlueFlagToNextPanelEnabled"] == '1':             settings |= 0x020  # BlueFlagToNextPanelEnabled
        if row["MarshalConsoleYellowSlipperyEnabled"] == '1':                  settings |= 0x040  # YellowSlipperyEnabled
        if row["MarshalConsoleRainAsFlagEnabled"] == '1':                      settings |= 0x080  # RainAsFlagEnabled
        if row["MarshalConsoleYellowDoubleYellowWhenSCandVSCEnabled"] == '1':  settings |= 0x100  # YellowDoubleYellowWhenSCandVSCEnabled
        if row["MarshalConsoleYellowDoubleYellowWhenSlowDownZone"] == '1':     settings |= 0x200  # YellowDoubleYellowWhenSlowDownZone
        c.marshal_console_settings = settings
        

        red_flag_policy = 0
        if row["RedFlagSectorPolicyAllowYellow"] == '1': red_flag_policy |= 0x1  # AllowYellow
        if row["RedFlagSectorPolicyLeaveYellow"] == '1': red_flag_policy |= 0x2  # LeaveYellow
        c.red_flag_policy = red_flag_policy

        c.safety_car_policy            = row["SafetyCarSectorPolicies"]
        c.rolling_start_speed_settings = row["RollingStartSpeedSettings"]   

        return c

    def _write_(self, new_cursor, circuits: list[Circuit]):

        new_cursor.execute("DELETE FROM t_circuits")

        sql = """
            INSERT INTO t_circuits (
                ID,
                CircuitNumber,
                Name,
                Active,
                MapFileName,
                MapFileMD5,
                SMMapFileName,
                SMMapFileMD5,
                SMMapFileHash,
                FlagSet,
                Password,
                StartingLightsControlUnitId,
                AksTimingServerId,
                TrackSidePanelBrightness,
                InfoPanelBrightness,
                PitlanePanelBrightness,
                TLABlueFlagRendering,
                InfoPanelRendering,
                MarshalConsoleSettings,
                WhiteButtonMode,
                CarBlueFlagFollowOnPanels,
                CarBlueFlagShow,
                RedFlagPolicy,
                SafetyCarPolicy,
                TimingMasterRole,
                UseYellowFlagForFCYEnabled,
                TrackPanelsBlacksDisplayMode,
                UseThreeStripesYellowRedFlagEnabled,
                RollingStartSpeedSettings
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [c.to_db_tuple() for c in circuits])
        Logger.info(f"Written {len(circuits)} circuits to t_circuits")