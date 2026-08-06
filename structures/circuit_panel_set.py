class CircuitPanelSet:

    def __init__(self):
        self.id:         int | None = None  # <- SetId
        self.circuit_id: int | None = None  # <- MapId
        self.name:       str | None = None
        self.panels:     str | None = None  # <- List

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.name,
            self.panels,
        )

    def __repr__(self):
        return f"CircuitPanelSet(id={self.id}, circuit_id={self.circuit_id}, name={self.name!r})"