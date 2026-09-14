from structures.circuit_slow_down_zone import CircuitSlowDownZone
from services.logger import Logger


class CircuitSlowDownZonesMapper:

    def _read_(self, old_cursor) -> list[CircuitSlowDownZone]:
        old_cursor.execute("SELECT * FROM t_slow_zones")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_slow_zones")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> CircuitSlowDownZone:
        z = CircuitSlowDownZone()
        z.id                  = row["Number"]
        z.circuit_id          = row["MapId"]
        z.first_sector_number = row["FirstSectorNumber"]
        z.last_sector_number  = row["LastSectorNumber"]
        return z

    def _write_(self, new_cursor, zones: list[CircuitSlowDownZone]):
        new_cursor.execute("DELETE FROM t_circuit_slow_down_zones")
        sql = """
            INSERT INTO t_circuit_slow_down_zones (
                ID, CircuitID, FirstSectorNumber, LastSectorNumber
            ) VALUES (?,?,?,?)
        """
        new_cursor.executemany(sql, [z.to_db_tuple() for z in zones])
        Logger.ok(f"Written {len(zones)} records to t_circuit_slow_down_zones")