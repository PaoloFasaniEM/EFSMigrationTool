class SessionManagerFeeder:

    def __init__(self):
        self.id:       int | None = None
        self.active:   int | None = None
        self.address:  str | None = None
        self.port:     int | None = None
        self.username: str | None = None 
        self.password: str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
            self.address,
            self.port,
            self.username,
            self.password,
        )

    def __repr__(self):
        return (
            f"SessionManagerFeeder(id={self.id}, "
            f"address={self.address!r}, port={self.port}, active={self.active})"
        )