class SavedGridCountdown:

    def __init__(self):
        self.id:               int | None = None
        self.name:             str | None = None
        self.countdown_time:   int | None = None
        self.message_duration: int | None = None
        self.autostart_time:   int | None = None
        self.messages:         str | None = None

    def to_db_tuple(self):
        return (
            self.id, self.name, self.countdown_time,
            self.message_duration, self.autostart_time, self.messages,
        )

    def __repr__(self):
        return f"SavedGridCountdown(id={self.id}, name={self.name!r})"