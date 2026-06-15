class ThirdPartyScu:

    def __init__(self):
        self.id:     int | None = None
        self.active: int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
        )

    def __repr__(self):
        return f"ThirdPartyScu(id={self.id}, active={self.active})"