from structures.saved_rule_set_alternative_group import SavedRuleSetAlternativeGroup
from services.logger import Logger


class SavedRuleSetsAlternativeGroupsMapper:

    def _read_(self, old_cursor) -> list[SavedRuleSetAlternativeGroup]:
        old_cursor.execute("SELECT * FROM t_maps_alternative_rule_groups")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_maps_alternative_rule_groups")

        result = []
        for row in rows:
            r = SavedRuleSetAlternativeGroup()
            r.id                = row["GroupId"]
            r.rule_set_id       = row["MapsRuleSetId"]
            r.group_name        = row["GroupName"]
            r.enabled_rule_name = row["EnabledRuleName"]
            result.append(r)

        return result

    def _write_(self, new_cursor, records: list[SavedRuleSetAlternativeGroup]):
        new_cursor.execute("DELETE FROM t_saved_rule_sets_alternative_groups")
        new_cursor.executemany(
            "INSERT INTO t_saved_rule_sets_alternative_groups (ID, RuleSetID, GroupName, EnabledRuleName) VALUES (?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_saved_rule_sets_alternative_groups")