class SavedRuleSetDisabled:

    def __init__(self):
        self.id:          int | None = None  # <- RuleId
        self.rule_set_id: int | None = None  # <- MapsRuleSetId
        self.short_name:  str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.rule_set_id,
            self.short_name,
        )

    def __repr__(self):
        return (
            f"SavedRuleSetDisabled(id={self.id}, "
            f"rule_set_id={self.rule_set_id}, short_name={self.short_name!r})"
        )