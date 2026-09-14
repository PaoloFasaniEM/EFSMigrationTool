from structures.circuit_panel import CircuitPanel
from services.logger import Logger


class CircuitPanelsMapper:

    def _read_(self, old_cursor) -> list[CircuitPanel]:

        old_cursor.execute("SELECT * FROM t_panels")
        panel_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(panel_rows)} records in t_panels")

        old_cursor.execute("SELECT * FROM t_panel_names")
        name_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(name_rows)} records in t_panel_names")

        # indice (map_id, panel_id) -> name
        names: dict[tuple, str] = {
            (row["MapId"], row["PanelId"]): row["Name"]
            for row in name_rows
        }

        result = []

        for row in panel_rows:
            p = CircuitPanel()
            p.id                = row["PanelId"]
            p.circuit_id        = row["MapId"]
            p.panel_name        = names.get((row["MapId"], row["PanelId"]), "")
            p.flags_allowed     = row["FlagsAllowed"]
            p.silent_mode       = row["SilentModeEnabled"]
            p.pit_sector        = row["PitSector"]
            p.messages_enabled  = row["MessagesEnabled"]
            p.timing_enabled    = row["TimingEnabled"]
            p.check_rc_connected = row["CheckRCConnected"]
            p.timing_outputs    = row["TimingOutputs"]
            result.append(p)

        return result

    def _write_(self, new_cursor, panels: list[CircuitPanel]):

        new_cursor.execute("DELETE FROM t_circuit_panels")

        sql = """
            INSERT INTO t_circuit_panels (
                ID, CircuitID, PanelName,
                FlagsAllowed, SilentMode, PitSector,
                MessagesEnabled, TimingEnabled, CheckRCConnected, TimingOutputs
            ) VALUES (?,?,?,?,?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [p.to_db_tuple() for p in panels])
        Logger.ok(f"Written {len(panels)} records to t_circuit_panels")