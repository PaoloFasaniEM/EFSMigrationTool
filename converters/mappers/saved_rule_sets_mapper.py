from structures.saved_rule_set import SavedRuleSet
from services.logger import Logger


class SavedRuleSetsMapper:

    def _read_(self, old_cursor) -> list[SavedRuleSet]:
        old_cursor.execute("SELECT * FROM t_maps_rule_sets")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_maps_rule_sets")

        result = []
        for row in rows:
            if not row["Name"]:
                continue
            r = SavedRuleSet()
            r.rule_set_id = row["ID"]
            r.name        = row["Name"]
            r.flag_set    = row["FlagSet"]
            result.append(r)

        return result

    def _write_(self, new_cursor, records: list[SavedRuleSet]):
        new_cursor.execute("DELETE FROM t_saved_rule_sets")
        new_cursor.executemany(
            "INSERT INTO t_saved_rule_sets (RuleSetID, Name, FlagSet) VALUES (?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_saved_rule_sets")