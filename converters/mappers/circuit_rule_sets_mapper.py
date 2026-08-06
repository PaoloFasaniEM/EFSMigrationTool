from structures.circuit_rule_set import CircuitRuleSet
from services.logger import Logger

INVALID_FLAG_SET = 2


class CircuitRuleSetsMapper:

    def _read_(self, old_cursor) -> list[CircuitRuleSet]:
        old_cursor.execute("SELECT * FROM t_rule_sets")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_rule_sets")

        result = []
        for row in rows:
            if int(row["FlagSet"]) == INVALID_FLAG_SET:
                continue
            r = CircuitRuleSet()
            r.id         = row["SetId"]
            r.circuit_id = row["MapId"]
            r.name       = row["Name"]
            r.flag_set   = row["FlagSet"]
            result.append(r)

        return result

    def _write_(self, new_cursor, records: list[CircuitRuleSet]):
        new_cursor.execute("DELETE FROM t_circuit_rule_sets")
        new_cursor.executemany(
            "INSERT INTO t_circuit_rule_sets (ID, CircuitID, Name, FlagSet) VALUES (?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_circuit_rule_sets")