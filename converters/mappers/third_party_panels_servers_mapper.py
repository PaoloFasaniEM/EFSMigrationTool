from structures.third_party_panels_server import ThirdPartyPanelsServer
from services.logger import Logger

class ThirdPartyPanelsServersMapper:

    def _read_(self, old_cursor) -> list[ThirdPartyPanelsServer]:

        old_cursor.execute("SELECT * FROM t_third_party_panels_servers")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_third_party_panels_servers")

        servers = [self._map_row(row) for row in rows]

        #for s in servers:
        #    print(s)

        return servers

    def _map_row(self, row) -> ThirdPartyPanelsServer:

        s = ThirdPartyPanelsServer()

        s.id       = row["ID"]
        s.active   = row["Active"]
        s.address  = row["Address"]
        s.port     = row["Port"]
        s.username = row["User"]
        s.password = row["Password"]

        return s

    def _write_(self, new_cursor, servers: list[ThirdPartyPanelsServer]):

        new_cursor.execute("DELETE FROM t_third_party_panels_servers")

        sql = """
            INSERT INTO t_third_party_panels_servers (
                ID, Active, Address, Port, Username, Password
            ) VALUES (?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [s.to_db_tuple() for s in servers])
        Logger.info(f"Written {len(servers)} records to t_third_party_panels_servers")