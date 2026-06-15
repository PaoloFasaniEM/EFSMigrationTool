class CircuitSlowDownZone:

    def __init__(self):
        self.id:                  int | None = None
        self.circuit_id:          int | None = None
        self.first_sector_number: int | None = None
        self.last_sector_number:  int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.first_sector_number,
            self.last_sector_number,
        )

    def __repr__(self):
        return (
            f"CircuitSlowDownZone(id={self.id}, circuit_id={self.circuit_id}, "
            f"sectors={self.first_sector_number}-{self.last_sector_number})"
        )