class CircuitPanel:

    def __init__(self):
        self.id:               int | None = None  # <- PanelId
        self.circuit_id:       int | None = None  # <- MapId
        self.panel_name:       str        = ""    # <- da t_panel_names
        self.flags_allowed:    int | None = None
        self.silent_mode:      int | None = None
        self.pit_sector:       int | None = None
        self.messages_enabled: int | None = None
        self.timing_enabled:   int | None = None
        self.check_rc_connected: int | None = None
        self.timing_outputs:   int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.panel_name,
            self.flags_allowed,
            self.silent_mode,
            self.pit_sector,
            self.messages_enabled,
            self.timing_enabled,
            self.check_rc_connected,
            self.timing_outputs,
        )

    def __repr__(self):
        return (
            f"CircuitPanel(id={self.id}, circuit_id={self.circuit_id}, "
            f"panel_name={self.panel_name!r})"
        )