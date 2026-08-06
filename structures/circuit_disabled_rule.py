class CircuitDisabledRule:

    def __init__(self):
        self.id:         int | None = None  # <- RuleId
        self.circuit_id: int | None = None  # <- MapId
        self.flag_set:   int | None = None
        self.short_name: str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.flag_set,
            self.short_name,
        )

    def __repr__(self):
        return (
            f"CircuitDisabledRule(id={self.id}, circuit_id={self.circuit_id}, "
            f"short_name={self.short_name!r})"
        )