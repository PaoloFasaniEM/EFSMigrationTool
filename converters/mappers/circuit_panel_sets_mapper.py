from structures.circuit_panel_set import CircuitPanelSet
from services.logger import Logger


class CircuitPanelSetsMapper:

    def _read_(self, old_cursor) -> list[CircuitPanelSet]:
        old_cursor.execute("SELECT * FROM t_panel_sets")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_panel_sets")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> CircuitPanelSet:
        p = CircuitPanelSet()
        p.id         = row["SetId"]
        p.circuit_id = row["MapId"]
        p.name       = row["Name"]
        p.panels     = row["List"]
        return p

    def _write_(self, new_cursor, records: list[CircuitPanelSet]):
        new_cursor.execute("DELETE FROM t_circuit_panel_sets")
        new_cursor.executemany(
            "INSERT INTO t_circuit_panel_sets (ID, CircuitID, Name, Panels) VALUES (?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_circuit_panel_sets")