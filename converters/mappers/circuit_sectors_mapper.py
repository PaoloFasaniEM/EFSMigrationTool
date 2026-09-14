from structures.circuit_sector import CircuitSector
from services.logger import Logger
from utils.db_utils import safe_int

class CircuitSectorsMapper:

    def _read_(self, old_cursor) -> list[CircuitSector]:

        old_cursor.execute("SELECT * FROM t_sector_propagations")
        prop_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(prop_rows)} records in t_sector_propagations")

        old_cursor.execute("SELECT * FROM t_slow_zones")
        sdz_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(sdz_rows)} records in t_slow_zones")

        sectors: dict[tuple, CircuitSector] = {}

        for row in prop_rows:
            circuit_id  = row["MapId"]
            sector_id   = row["SectorNumber"]
            key         = (circuit_id, sector_id)

            s = CircuitSector()
            s.id          = sector_id
            s.circuit_id  = circuit_id
            s.propagation = row["Propagation"]
            s.prev_flags  = row["PrevFlags"]
            s.next_flags  = row["NextFlags"]
            s.sdz_number  = 0

            sectors[key] = s

        for row in sdz_rows:
            circuit_id = row["MapId"]
            sdz_number = row["Number"]
            first      = safe_int(row["FirstSectorNumber"])
            last       = safe_int(row["LastSectorNumber"])

            for sector_id in range(first, last + 1):
                key = (circuit_id, sector_id)

                if key in sectors:
                    sectors[key].sdz_number = sdz_number
                else:
                    s = CircuitSector()
                    s.id          = sector_id
                    s.circuit_id  = circuit_id
                    s.propagation = 0
                    s.prev_flags  = 0
                    s.next_flags  = 0
                    s.sdz_number  = sdz_number
                    sectors[key]  = s

        result = list(sectors.values())
        Logger.info(f"Composed {len(result)} circuit sectors")
        return result

    def _write_(self, new_cursor, sectors: list[CircuitSector]):
        new_cursor.execute("DELETE FROM t_circuit_sectors")
        sql = """
            INSERT INTO t_circuit_sectors (
                ID, CircuitID, Propagation, PrevFlags, NextFlags, SDZNumber
            ) VALUES (?,?,?,?,?,?)
        """
        new_cursor.executemany(sql, [s.to_db_tuple() for s in sectors])
        Logger.ok(f"Written {len(sectors)} records to t_circuit_sectors")