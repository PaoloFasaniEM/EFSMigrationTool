class CircuitInfoPanelPenaltyRendering:

    def __init__(self):
        self.id:               int | None = None  
        self.circuit_id:       int | None = None  # <- MapId
        self.penalty:          int | None = None  # <- converted via FlagPageParams
        self.text_color:       int | None = None
        self.background_color: int | None = None
        self.flashing_mode:    int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.penalty,
            self.text_color,
            self.background_color,
            self.flashing_mode,
        )

    def __repr__(self):
        return (
            f"CircuitInfoPanelPenaltyRendering(id={self.id}, "
            f"circuit_id={self.circuit_id}, penalty={self.penalty})"
        )