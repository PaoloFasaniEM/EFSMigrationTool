class VICFlagHexCode:

    def __init__(self):
        self.id:            int | None = None
        self.flag:          int | None = None
        self.number:        int | None = None
        self.frequency:     int | None = None
        self.silent:        int | None = None
        self.graphical_code: str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.flag,
            self.number,
            self.frequency,
            self.silent,
            self.graphical_code,
        )

    def __repr__(self):
        return (
            f"VICFlagHexCode(id={self.id}, flag={self.flag}, "
            f"frequency={self.frequency}, graphical_code={self.graphical_code!r})"
        )