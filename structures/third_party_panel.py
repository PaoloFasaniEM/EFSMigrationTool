class ThirdPartyPanel:

    def __init__(self):
        self.id:           int | None = None
        self.active:       int | None = None
        self.name:         str | None = None
        self.panel_type:   int | None = None
        self.aspect_ratio: int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
            self.name,
            self.panel_type,
            self.aspect_ratio,
        )

    def __repr__(self):
        return (
            f"ThirdPartyPanel(id={self.id}, name={self.name!r}, "
            f"panel_type={self.panel_type}, active={self.active})"
        )