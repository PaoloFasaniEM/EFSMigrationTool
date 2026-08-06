class Championship:

    def __init__(self):
        self.id:                   int | None = None
        self.short_name:           str | None = None
        self.full_name:            str | None = None
        self.timing_name:          str | None = None
        self.smart_marshalling_id: str        = ""

    def to_db_tuple(self):
        return (
            self.id,
            self.short_name,
            self.full_name,
            self.timing_name,
            self.smart_marshalling_id,
        )

    def __repr__(self):
        return f"Championship(id={self.id}, short_name={self.short_name!r})"