from structures.car import Car
from services.logger import Logger


class CarsMapper:

    def _read_(self, old_cursor) -> list[Car]:

        old_cursor.execute("SELECT * FROM t_usb_cars")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_usb_cars")

        cars = [self._map_row(row) for row in rows]

        return cars

    def _map_row(self, row) -> Car:

        c = Car()

        c.id                       = row["ID"]
        c.type                     = row["Type"]
        c.active                   = row["Active"]
        c.circuit_number           = row["UsbGroups"]
        c.number                   = row["Number"]
        c.label                    = row["Label"]
        c.all_championship_allowed = row["AllChampionshipsAllowed"]
        c.championship_name        = row["ChampionshipName"]
        c.fixed_circuit_number     = row["FixUsbGroups"]
        c.default_circuit_number   = row["DefaultUsbGroup"]

        return c

    def _write_(self, new_cursor, cars: list[Car]):

        new_cursor.execute("DELETE FROM t_cars")

        sql = """
            INSERT INTO t_cars (
                ID, Type, Active, CircuitNumber, Number, Label,
                AllChampionshipAllowed, ChampionshipName,
                FixedCircuitNumber, DefaultCircuitNumber
            ) VALUES (?,?,?,?,?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [c.to_db_tuple() for c in cars])
        Logger.info(f"Written {len(cars)} records to t_cars")