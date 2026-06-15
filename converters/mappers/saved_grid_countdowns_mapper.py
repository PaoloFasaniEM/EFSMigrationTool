from structures.saved_grid_countdown import SavedGridCountdown
from services.logger import Logger

class SavedGridCountdownsMapper:

    def _read_(self, old_cursor) -> list[SavedGridCountdown]:
        old_cursor.execute("SELECT * FROM t_saved_grid_countdowns")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_saved_grid_countdowns")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> SavedGridCountdown:
        g = SavedGridCountdown()
        g.id               = row["ID"]
        g.name             = row["Name"]
        g.countdown_time   = row["CountdownTime"]
        g.message_duration = row["MessageDuration"]
        g.autostart_time   = row["AutostartTime"]
        g.messages         = row["Messages"]
        return g

    def _write_(self, new_cursor, countdowns: list[SavedGridCountdown]):
        new_cursor.execute("DELETE FROM t_saved_grid_countdowns")
        sql = """
            INSERT INTO t_saved_grid_countdowns (
                ID, Name, CountdownTime, MessageDuration, AutostartTime, Messages
            ) VALUES (?,?,?,?,?,?)
        """
        new_cursor.executemany(sql, [g.to_db_tuple() for g in countdowns])
        Logger.ok(f"Written {len(countdowns)} records to t_saved_grid_countdowns")