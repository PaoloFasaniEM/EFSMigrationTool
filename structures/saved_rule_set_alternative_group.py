class SavedRuleSetAlternativeGroup:

    def __init__(self):
        self.id:                int | None = None  # <- GroupId
        self.rule_set_id:       int | None = None  # <- MapsRuleSetId
        self.group_name:        str | None = None
        self.enabled_rule_name: str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.rule_set_id,
            self.group_name,
            self.enabled_rule_name,
        )

    def __repr__(self):
        return (
            f"SavedRuleSetAlternativeGroup(id={self.id}, "
            f"rule_set_id={self.rule_set_id}, group_name={self.group_name!r})"
        )