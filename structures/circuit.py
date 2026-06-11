
class Circuit:
    """
    Struttura dati intermedia per un circuito convertito da t_maps → t_circuits.
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
        self.marshal_console_settings: int | None = None      # TODO: logica di conversione
        self.white_button_mode: int | None = None             # TODO: da MarshalConsoleWhiteButtonMode?
        self.car_blue_flag_follow_on_panels: int | None = None  # TODO: da AutoBlueFlagFollowOnPanels?
        self.car_blue_flag_show: int | None = None            # TODO: da AutoBlueFlagVisualizationMode?
        self.red_flag_policy: int | None = None               # TODO: da RedFlagSectorPolicy*?

    def to_db_tuple(self):
        
        return (
            self.id,
            self.circuit_number,
            self.name,
            self.active,
            self.map_file_name,
            self.map_file_md5,
            self.sm_map_file_name,
            self.sm_map_file_md5,
            self.sm_map_file_hash,
            self.flag_set,
            self.password,
            self.starting_lights_control_unit_id,
            self.aks_timing_server_id,
            self.track_side_panel_brightness,
            self.info_panel_brightness,
            self.pitlane_panel_brightness,
            self.tla_blue_flag_rendering,
            self.info_panel_rendering,
            self.marshal_console_settings,
            self.white_button_mode,
            self.car_blue_flag_follow_on_panels,
            self.car_blue_flag_show,
            self.red_flag_policy,
            self.timing_master_role,
            self.use_yellow_flag_for_fcy_enabled,
            self.track_panels_blacks_display_mode,
            self.use_three_stripes_yellow_red_flag_enabled
        )

    def __repr__(self):
        return (
            f"Circuit(id={self.id}, name={self.name!r}, "
            f"circuit_number={self.circuit_number}, active={self.active})"
        )

