from structures.session_manager_feeder import SessionManagerFeeder
from services.logger import Logger

class SessionManagerFeedersMapper:

    def _read_(self, old_cursor) -> list[SessionManagerFeeder]:

        old_cursor.execute("SELECT * FROM t_session_manager")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_session_manager")

        feeders = [self._map_row(row) for row in rows]

        #for c in feeders:
        #    print(c)

        return feeders

    def _map_row(self, row) -> SessionManagerFeeder:

        c = SessionManagerFeeder()

        c.id       = row["ID"]
        c.active   = row["Active"]
        c.address  = row["Address"]
        c.port     = row["Port"]
        c.username = row["User"]
        c.password = row["Password"]

        return c

    def _write_(self, new_cursor, feeders: list[SessionManagerFeeder]):

        new_cursor.execute("DELETE FROM t_session_manager_feeders")

        sql = """
            INSERT INTO t_session_manager_feeders (
                ID, Active, Address, Port, Username, Password
            ) VALUES (?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [c.to_db_tuple() for c in feeders])
        Logger.info(f"Written {len(feeders)} records to t_session_manager_feeders")