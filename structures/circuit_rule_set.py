class CircuitRuleSet:

    def __init__(self):
        self.id:         int | None = None  # <- SetId
        self.circuit_id: int | None = None  # <- MapId
        self.name:       str | None = None
        self.flag_set:   int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.name,
            self.flag_set,
        )

    def __repr__(self):
        return f"CircuitRuleSet(id={self.id}, circuit_id={self.circuit_id}, name={self.name!r})"