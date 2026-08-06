class CircuitFlagMode:

    def __init__(self):
        self.id:                int | None = None  # <- Flag + 1
        self.circuit_id:        int | None = None  # <- MapId
        self.click_mode:        int | None = None
        self.double_click_mode: int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.click_mode,
            self.double_click_mode,
        )

    def __repr__(self):
        return (
            f"CircuitFlagMode(id={self.id}, circuit_id={self.circuit_id}, "
            f"click={self.click_mode}, double_click={self.double_click_mode})"
        )