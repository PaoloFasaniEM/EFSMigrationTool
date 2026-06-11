class EMInfoPanel:

    def __init__(self):
        self.id:      int | None = None
        self.active:  int | None = None
        self.model:   int | None = None
        self.size:    int | None = None
        self.name:    str | None = None
        self.address: str | None = None
        self.port:    int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
            self.model,
            self.size,
            self.name,
            self.address,
            self.port,
        )

    def __repr__(self):
        return (
            f"EMInfoPanel(id={self.id}, name={self.name!r}, "
            f"active={self.active})"
        )