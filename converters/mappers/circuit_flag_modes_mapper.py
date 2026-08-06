from structures.circuit_flag_mode import CircuitFlagMode
from services.logger import Logger

class CircuitFlagModesMapper:

    def _read_(self, old_cursor) -> list[CircuitFlagMode]:
        old_cursor.execute("SELECT * FROM t_marshal_console_button_flag_modes")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_marshal_console_button_flag_modes")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> CircuitFlagMode:
        f = CircuitFlagMode()
        f.id                = int(row["Flag"]) + 1
        f.circuit_id        = row["MapId"]
        f.click_mode        = row["ClickMode"]
        f.double_click_mode = row["DoubleClickMode"]
        return f

    def _write_(self, new_cursor, modes: list[CircuitFlagMode]):
        new_cursor.execute("DELETE FROM t_circuit_flag_modes")
        sql = """
            INSERT INTO t_circuit_flag_modes (
                ID, CircuitID, ClickMode, DoubleClickMode
            ) VALUES (?,?,?,?)
        """
        new_cursor.executemany(sql, [m.to_db_tuple() for m in modes])
        Logger.ok(f"Written {len(modes)} records to t_circuit_flag_modes")