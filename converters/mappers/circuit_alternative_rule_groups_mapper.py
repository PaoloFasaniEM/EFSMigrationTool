from structures.circuit_alternative_rule_group import CircuitAlternativeRuleGroup
from services.logger import Logger

INVALID_FLAG_SET = 2


class CircuitAlternativeRuleGroupsMapper:

    def _read_(self, old_cursor) -> list[CircuitAlternativeRuleGroup]:
        old_cursor.execute("SELECT * FROM t_alternative_rule_groups")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_alternative_rule_groups")

        result = []
        for row in rows:
            if int(row["FlagSet"]) == INVALID_FLAG_SET:
                continue
            r = CircuitAlternativeRuleGroup()
            r.id                = row["GroupId"]
            r.circuit_id        = row["MapId"]
            r.flag_set          = row["FlagSet"]
            r.group_name        = row["GroupName"]
            r.enabled_rule_name = row["EnabledRuleName"]
            result.append(r)

        return result

    def _write_(self, new_cursor, records: list[CircuitAlternativeRuleGroup]):
        new_cursor.execute("DELETE FROM t_circuit_alternative_rule_groups")
        new_cursor.executemany(
            "INSERT INTO t_circuit_alternative_rule_groups (ID, CircuitID, FlagSet, GroupName, EnabledRuleName) VALUES (?,?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_circuit_alternative_rule_groups")