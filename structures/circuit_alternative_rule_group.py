class CircuitAlternativeRuleGroup:

    def __init__(self):
        self.id:                int | None = None  # <- GroupId
        self.circuit_id:        int | None = None  # <- MapId
        self.flag_set:          int | None = None
        self.group_name:        str | None = None
        self.enabled_rule_name: str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.circuit_id,
            self.flag_set,
            self.group_name,
            self.enabled_rule_name,
        )

    def __repr__(self):
        return (
            f"CircuitAlternativeRuleGroup(id={self.id}, "
            f"circuit_id={self.circuit_id}, group_name={self.group_name!r})"
        )