from structures.alkamel_timing import AlkamelTiming
from services.logger import Logger

class AlkamelTimingMapper:

    def _read_(self, old_cursor) -> list[AlkamelTiming]:

        old_cursor.execute("SELECT * FROM t_alkamel_timing")
        rows = old_cursor.fetchall()
        
        Logger.info(f"Found {len(rows)} records in t_alkamel_timing")

        timings = [self._map_row_(row) for row in rows]

        #for t in timings:
        #    print(t)

        return timings

    def _map_row_(self, row) -> AlkamelTiming:

        t = AlkamelTiming()

        t.id               = row["ID"]
        t.active           = row["Active"]
        t.address          = row["Address"]
        t.port             = row["Port"]
        t.user             = row["User"]
        t.password         = row["Password"]
        t.protocol_version = row["ProtocolVersion"]

        return t

    def _write_(self, new_cursor, timings: list[AlkamelTiming]):

        new_cursor.execute("DELETE FROM t_alkamel_timing")

        sql = """
            INSERT INTO t_alkamel_timing (
                ID, Active, Address, Port, User, Password, ProtocolVersion
            ) VALUES (?,?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [t.to_db_tuple() for t in timings])
        Logger.info(f"Written {len(timings)} records to t_alkamel_timing")