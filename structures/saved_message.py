class SavedMessage:

    def __init__(self):
        self.id:               int | None = None
        self.name:             str | None = None
        self.width:            int | None = None
        self.height:           int | None = None
        self.font_size:        int | None = None
        self.font_style:       int | None = None
        self.horz_alignment:   int | None = None
        self.vert_alignment:   int | None = None
        self.x_margin:         int | None = None
        self.y_margin:         int | None = None
        self.text_color:       str | None = None
        self.background_color: str | None = None
        self.message:          str | None = None

    def to_db_tuple(self):
        return (
            self.id, self.name, self.width, self.height,
            self.font_size, self.font_style, self.horz_alignment,
            self.vert_alignment, self.x_margin, self.y_margin,
            self.text_color, self.background_color, self.message,
        )

    def __repr__(self):
        return f"SavedMessage(id={self.id}, name={self.name!r})"