from structures.saved_session import SavedSession
from services.logger import Logger

class SavedSessionsMapper:

    def _read_(self, old_cursor) -> list[SavedSession]:
        old_cursor.execute("SELECT * FROM t_saved_sessions")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_saved_sessions")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> SavedSession:
        s = SavedSession()
        s.id                         = row["ID"]
        s.name                       = row["Name"]
        s.type                       = row["Type"]
        s.champ_short_name           = row["ChampShortName"]
        s.mode                       = row["Mode"]
        s.duration_secs              = row["DurationSecs"]
        s.laps                       = row["Laps"]
        s.stop_time_when_suspended   = row["StopTimeWhenSuspended"]
        s.finish_when_countdown_ends = row["FinishWhenCountdownEnds"]
        s.recording_enabled          = row["RecordingEnabled"]
        s.show_laps_and_running_time = row["ShowLapsAndRunningTime"]
        s.schedule_mode              = row["ScheduleMode"]
        s.session_date               = row["SessionDate"]
        s.session_open_time          = row["SessionOpenTime"]
        s.session_start_time         = row["SessionStartTime"]
        s.circuit_group              = row["CircuitGroup"]
        return s

    def _write_(self, new_cursor, sessions: list[SavedSession]):
        new_cursor.execute("DELETE FROM t_saved_sessions")
        sql = """
            INSERT INTO t_saved_sessions (
                ID, Name, Type, ChampShortName, Mode, DurationSecs, Laps,
                StopTimeWhenSuspended, FinishWhenCountdownEnds, RecordingEnabled,
                ShowLapsAndRunningTime, ScheduleMode, SessionDate,
                SessionOpenTime, SessionStartTime, CircuitGroup
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """
        new_cursor.executemany(sql, [s.to_db_tuple() for s in sessions])
        Logger.ok(f"Written {len(sessions)} records to t_saved_sessions")