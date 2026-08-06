class CircuitSector:

    def __init__(self):
        self.id:          int | None = None   # <- SectorNumber
        self.circuit_id:  int | None = None   # <- MapId
        self.propagation: int | None = None
        self.prev_flags:  int | None = None
        self.next_flags:  int | None = None
        self.sdz_number:  int | None = None   # 0 se non è in una SDZ

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.propagation,
            self.prev_flags,
            self.next_flags,
            self.sdz_number,
        )

    def __repr__(self):
        return (
            f"CircuitSector(id={self.id}, circuit_id={self.circuit_id}, "
            f"propagation={self.propagation}, sdz={self.sdz_number})"
        )