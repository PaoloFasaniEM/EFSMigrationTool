
class AlkamelTiming:

    def __init__(self):
        self.id: int | None = None
        self.active: int | None = None
        self.address: str | None = None
        self.port: int | None = None
        self.user: str | None = None
        self.password: str | None = None
        self.protocol_version: str | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
            self.address,
            self.port,
            self.user,
            self.password,
            self.protocol_version,
        )

    def __repr__(self):
        return (
            f"AlkamelTiming(id={self.id}, address={self.address!r}, "
            f"port={self.port}, active={self.active})"
        )
