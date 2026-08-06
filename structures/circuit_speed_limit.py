class CircuitSpeedLimit:

    def __init__(self):
        self.id:                    int | None = None  # <- new flag + 1
        self.circuit_id:            int | None = None  # <- MapId
        self.in_use:                int | None = None
        self.speed:                 int | None = None
        self.speed_unit:            int | None = None
        self.max_overspeed_secs:    int | None = None
        self.detected_by_unit:      int | None = None
        self.create_report:         int | None = None  # <- Report

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.in_use,
            self.speed,
            self.speed_unit,
            self.max_overspeed_secs,
            self.detected_by_unit,
            self.create_report,
        )

    def __repr__(self):
        return (
            f"CircuitSpeedLimit(id={self.id}, circuit_id={self.circuit_id}, "
            f"speed={self.speed}, in_use={self.in_use})"
        )