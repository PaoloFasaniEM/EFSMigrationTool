class SavedSession:

    def __init__(self):
        self.id:                            int | None = None
        self.name:                          str | None = None
        self.type:                          int | None = None
        self.champ_short_name:              str | None = None
        self.mode:                          int | None = None
        self.duration_secs:                 int | None = None
        self.laps:                          int | None = None
        self.stop_time_when_suspended:      int | None = None
        self.finish_when_countdown_ends:    int | None = None
        self.recording_enabled:             int | None = None
        self.show_laps_and_running_time:    int | None = None
        self.schedule_mode:                 int | None = None
        self.session_date:                  str | None = None
        self.session_open_time:             str | None = None
        self.session_start_time:            str | None = None
        self.circuit_group:                 int | None = None

    def to_db_tuple(self):
        return (
            self.id, self.name, self.type, self.champ_short_name,
            self.mode, self.duration_secs, self.laps,
            self.stop_time_when_suspended, self.finish_when_countdown_ends,
            self.recording_enabled, self.show_laps_and_running_time,
            self.schedule_mode, self.session_date, self.session_open_time,
            self.session_start_time, self.circuit_group,
        )

    def __repr__(self):
        return f"SavedSession(id={self.id}, name={self.name!r}, type={self.type})"