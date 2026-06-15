from structures.starting_lights_control_unit import StartingLightsControlUnit
from structures.third_party_scu import ThirdPartyScu
from services.logger import Logger


class StartingLightsControlUnitsMapper:

    def _read_(self, old_cursor) -> tuple[list[StartingLightsControlUnit], list[ThirdPartyScu]]:

        old_cursor.execute("SELECT * FROM t_starting_light_control_units")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_starting_light_control_units")

        scus        = []
        third_party = []

        for row in rows:
            if int(row["ThirdParty"]):
                third_party.append(self._map_row_to_third_party(row))
            else:
                scus.append(self._map_row_to_scu(row))

        Logger.info(f"  → {len(scus)} standard SCUs")
        Logger.info(f"  → {len(third_party)} third party SCUs")

        return scus, third_party

    def _map_row_to_scu(self, row) -> StartingLightsControlUnit:

        s = StartingLightsControlUnit()

        s.id      = row["ID"]
        s.active  = row["Active"]
        s.address = row["Address"]
        s.port    = row["Port"]

        return s

    def _map_row_to_third_party(self, row) -> ThirdPartyScu:

        t = ThirdPartyScu()

        t.id     = row["ID"]
        t.active = row["Active"]

        return t

    def _write_(self, new_cursor,
                scus: list[StartingLightsControlUnit],
                third_party: list[ThirdPartyScu]):

        new_cursor.execute("DELETE FROM t_starting_lights_control_units")

        sql_scu = """
            INSERT INTO t_starting_lights_control_units (
                ID, Active, Address, Port
            ) VALUES (?,?,?,?)
        """
        new_cursor.executemany(sql_scu, [s.to_db_tuple() for s in scus])
        Logger.ok(f"Written {len(scus)} records to t_starting_lights_control_units")

        new_cursor.execute("DELETE FROM t_third_party_scus")

        sql_tp = """
            INSERT INTO t_third_party_scus (
                ID, Active
            ) VALUES (?,?)
        """
        new_cursor.executemany(sql_tp, [t.to_db_tuple() for t in third_party])
        Logger.ok(f"Written {len(third_party)} records to t_third_party_scus")