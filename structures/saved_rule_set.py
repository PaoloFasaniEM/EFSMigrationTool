class SavedRuleSet:

    def __init__(self):
        self.rule_set_id: int | None = None  # <- ID
        self.name:        str | None = None
        self.flag_set:    int | None = None

    def to_db_tuple(self):
        return (
            self.rule_set_id,
            self.name,
            self.flag_set,
        )

    def __repr__(self):
        return f"SavedRuleSet(rule_set_id={self.rule_set_id}, name={self.name!r})"