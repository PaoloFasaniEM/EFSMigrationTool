
class Circuit:
    """
    Struttura dati intermedia per un circuito convertito da t_maps -> t_circuits.
    I campi con valore None sono da completare con logica custom.
    """

    def __init__(self):
        # Campi mappati direttamente o rinominati
        self.id: int | None = None
        self.circuit_number: int | None = None       # <- PanelGroup
        self.name: str | None = None
        self.active: int | None = None
        self.map_file_name: str | None = None        # <- MapFile
        self.map_file_md5: str | None = None
        self.sm_map_file_name: str | None = None     # <- SMMapFile
        self.sm_map_file_md5: str | None = None
        self.sm_map_file_hash: int | None = None     # <- MapHash
        self.flag_set: int | None = None
        self.password: str | None = None
        self.starting_lights_control_unit_id: int | None = None
        self.aks_timing_server_id: int | None = None
        self.track_side_panel_brightness: int | None = None   # <- TracksidePanelsBrightness
        self.info_panel_brightness: int | None = None         # <- InfoPanelsBrightness
        self.pitlane_panel_brightness: int | None = None      # <- PitlanePanelsBrightness
        self.tla_blue_flag_rendering: int | None = None       # <- CustomBlueFlagRendering
        self.info_panel_rendering: int | None = None
        self.timing_master_role: int | None = None            # <- CircuitTimingMasterRole
        self.use_yellow_flag_for_fcy_enabled: int | None = None
        self.track_panels_blacks_display_mode: int | None = None
        self.use_three_stripes_yellow_red_flag_enabled: int | None = None

        # Campi sospesi - da completare
        self.marshal_console_settings: int | None = None        
        self.white_button_mode: int | None = None              
        self.car_blue_flag_follow_on_panels: int | None = None  
        self.car_blue_flag_show: int | None = None              
        self.red_flag_policy: int | None = None
        self.safety_car_policy: int | None = None  # <- SafetyCarSectorPolicies
        self.rolling_start_speed_settings: int | None = None  # <- RollingStartSpeedSettings                 

    def to_db_tuple(self):
        return (
            self.id,                                        # 1
            self.circuit_number,                            # 2
            self.name,                                      # 3
            self.active,                                    # 4
            self.map_file_name,                             # 5
            self.map_file_md5,                              # 6
            self.sm_map_file_name,                          # 7
            self.sm_map_file_md5,                           # 8
            self.sm_map_file_hash,                          # 9
            self.flag_set,                                  # 10
            self.password,                                  # 11
            self.starting_lights_control_unit_id,           # 12
            self.aks_timing_server_id,                      # 13
            self.track_side_panel_brightness,               # 14
            self.info_panel_brightness,                     # 15
            self.pitlane_panel_brightness,                  # 16
            self.tla_blue_flag_rendering,                   # 17
            self.info_panel_rendering,                      # 18
            self.marshal_console_settings,                  # 19
            self.white_button_mode,                         # 20
            self.car_blue_flag_follow_on_panels,            # 21
            self.car_blue_flag_show,                        # 22
            self.red_flag_policy,                           # 23
            self.safety_car_policy,                         # 24
            self.timing_master_role,                        # 25
            self.use_yellow_flag_for_fcy_enabled,           # 26
            self.track_panels_blacks_display_mode,          # 27
            self.use_three_stripes_yellow_red_flag_enabled, # 28
            self.rolling_start_speed_settings,              # 29
        )

    def __repr__(self):
        return (
            f"Circuit(id={self.id}, name={self.name!r}, "
            f"circuit_number={self.circuit_number}, active={self.active})"
        )

