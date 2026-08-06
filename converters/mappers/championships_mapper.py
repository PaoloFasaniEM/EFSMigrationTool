from structures.championship import Championship
from services.logger import Logger


class ChampionshipsMapper:

    def _read_(self, old_cursor) -> list[Championship]:
        old_cursor.execute("SELECT * FROM t_championships")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_championships")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> Championship:
        c = Championship()
        c.id          = row["ID"]
        c.short_name  = row["ShortName"]
        c.full_name   = row["FullName"]
        c.timing_name = row["TimingName"]
        return c

    def _write_(self, new_cursor, records: list[Championship]):
        new_cursor.execute("DELETE FROM t_championships")
        new_cursor.executemany(
            "INSERT INTO t_championships (ID, ShortName, FullName, TimingName, SmartMarshallingId) VALUES (?,?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_championships")