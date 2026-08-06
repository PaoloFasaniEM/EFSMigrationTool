from structures.circuit_disabled_rule import CircuitDisabledRule
from services.logger import Logger


class CircuitDisabledRulesMapper:

    def _read_(self, old_cursor) -> list[CircuitDisabledRule]:

        old_cursor.execute("SELECT * FROM t_disabled_rules")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_disabled_rules")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> CircuitDisabledRule:

        r = CircuitDisabledRule()
        r.id         = row["RuleId"]
        r.circuit_id = row["MapId"]
        r.flag_set   = row["FlagSet"]
        r.short_name = row["ShortName"]
        return r

    def _write_(self, new_cursor, rules: list[CircuitDisabledRule]):

        new_cursor.execute("DELETE FROM t_circuit_disabled_rules")

        sql = """
            INSERT INTO t_circuit_disabled_rules (
                ID, CircuitID, FlagSet, ShortName
            ) VALUES (?,?,?,?)
        """

        new_cursor.executemany(sql, [r.to_db_tuple() for r in rules])
        Logger.ok(f"Written {len(rules)} records to t_circuit_disabled_rules")