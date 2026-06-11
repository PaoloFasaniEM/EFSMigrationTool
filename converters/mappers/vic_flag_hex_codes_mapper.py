from structures.vic_flag_hex_code import VICFlagHexCode
from services.logger import Logger

class VICFlagHexCodesMapper:

    def _read_(self, old_cursor) -> list[VICFlagHexCode]:

        old_cursor.execute("SELECT * FROM t_vic_flag_hex_codes")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_vic_flag_hex_codes")

        codes = [self._map_row(row) for row in rows]

        #for c in codes:
        #    print(c)

        return codes

    def _map_row(self, row) -> VICFlagHexCode:

        c = VICFlagHexCode()

        c.id             = row["ID"]
        c.flag           = row["Flag"]
        c.number         = row["Number"]
        c.frequency      = row["Frequency"]
        c.silent         = row["Silent"]
        c.graphical_code = row["GraphicalCode"]

        return c

    def _write_(self, new_cursor, codes: list[VICFlagHexCode]):

        new_cursor.execute("DELETE FROM t_vic_flag_hex_codes")

        sql = """
            INSERT INTO t_vic_flag_hex_codes (
                ID, Flag, Number, Frequency, Silent, GraphicalCode
            ) VALUES (?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [c.to_db_tuple() for c in codes])
        Logger.info(f"Written {len(codes)} records to t_vic_flag_hex_codes")