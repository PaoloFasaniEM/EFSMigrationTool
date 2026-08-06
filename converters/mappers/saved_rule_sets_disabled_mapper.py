from structures.saved_rule_set_disabled import SavedRuleSetDisabled
from services.logger import Logger


class SavedRuleSetsDisabledMapper:

    def _read_(self, old_cursor) -> list[SavedRuleSetDisabled]:
        old_cursor.execute("SELECT * FROM t_maps_disabled_rules")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_maps_disabled_rules")

        result = []
        for row in rows:
            r = SavedRuleSetDisabled()
            r.id          = row["RuleId"]
            r.rule_set_id = row["MapsRuleSetId"]
            r.short_name  = row["ShortName"]
            result.append(r)

        return result

    def _write_(self, new_cursor, records: list[SavedRuleSetDisabled]):
        new_cursor.execute("DELETE FROM t_saved_rule_sets_disabled")
        new_cursor.executemany(
            "INSERT INTO t_saved_rule_sets_disabled (ID, RuleSetID, ShortName) VALUES (?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_saved_rule_sets_disabled")