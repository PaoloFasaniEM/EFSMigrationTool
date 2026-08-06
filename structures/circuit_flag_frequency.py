class CircuitFlagFrequency:

    def __init__(self):
        self.id:         int | None = None
        self.circuit_id: int | None = None  
        self.frequency:  int | None = None
        self.silent:     int | None = None  

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.frequency,
            self.silent,
        )

    def __repr__(self):
        return (
            f"CircuitFlagFrequency(id={self.id}, circuit_id={self.circuit_id}, "
            f"frequency={self.frequency}, silent={self.silent})"
        )