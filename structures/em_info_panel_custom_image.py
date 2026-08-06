class EMInfoPanelCustomImage:

    def __init__(self):
        self.id:                    int | None = None
        self.name:                  str | None = None
        self.source_file_extension: str | None = None
        self.source_bitmap_md5:     str | None = None
        self.thumbnail_md5:         str | None = None
        self.background_color:      int | None = None
        self.type:                  int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.name,
            self.source_file_extension,
            self.source_bitmap_md5,
            self.thumbnail_md5,
            self.background_color,
            self.type,
        )

    def __repr__(self):
        return f"EMInfoPanelCustomImage(id={self.id}, name={self.name!r})"