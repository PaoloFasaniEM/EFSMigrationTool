from structures.smart_marshalling_client import SmartMarshallingClient
from services.logger import Logger

class SmartMarshallingClientsMapper:

    def _read_(self, old_cursor) -> list[SmartMarshallingClient]:

        old_cursor.execute("SELECT * FROM t_smart_marshalling")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_smart_marshalling")

        clients = [self._map_row(row) for row in rows]

        #for c in clients:
        #    print(c)

        return clients

    def _map_row(self, row) -> SmartMarshallingClient:

        c = SmartMarshallingClient()

        c.id       = row["ID"]
        c.active   = row["Active"]
        c.address  = row["Address"]
        c.port     = row["Port"]
        c.username = row["User"]   # rinominato
        c.password = row["Password"]

        return c

    def _write_(self, new_cursor, clients: list[SmartMarshallingClient]):

        new_cursor.execute("DELETE FROM t_smart_marshalling_clients")

        sql = """
            INSERT INTO t_smart_marshalling_clients (
                ID, Active, Address, Port, Username, Password
            ) VALUES (?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [c.to_db_tuple() for c in clients])
        Logger.info(f"Written {len(clients)} records to t_smart_marshalling_clients")