class CustomImage:

    def __init__(self):
        self.id:               int | None = None
        self.name:             str | None = None
        self.background_color: str | None = None  # RRGGBB
        self.type:             int | None = None   # 0=Logo, 1=Sign

    def to_db_tuple(self):
        return (
            self.id,
            self.name,
            self.background_color,
            self.type,
        )

    def __repr__(self):
        return f"CustomImage(id={self.id}, name={self.name!r}, type={self.type})"