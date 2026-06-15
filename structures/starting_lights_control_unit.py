class StartingLightsControlUnit:

    def __init__(self):
        self.id:      int | None = None
        self.active:  int | None = None
        self.address: str | None = None
        self.port:    int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
            self.address,
            self.port,
        )

    def __repr__(self):
        return (
            f"StartingLightsControlUnit(id={self.id}, "
            f"address={self.address!r}, port={self.port}, active={self.active})"
        )