class EMTPanel:

    def __init__(self):
        self.id:                    int | None = None
        self.active:                int | None = None
        self.model:                 int | None = None
        self.size:                  int | None = None
        self.name:                  str | None = None
        self.address:               str | None = None
        self.port:                  int | None = None
        self.upload_address:        str | None = None
        self.upload_port:           int | None = None
        self.marshal_remote_control: int | None = None  # <- HasMarshalRemoteControl

    def to_db_tuple(self):
        return (
            self.id,
            self.active,
            self.model,
            self.size,
            self.name,
            self.address,
            self.port,
            self.upload_address,
            self.upload_port,
            self.marshal_remote_control,
        )

    def __repr__(self):
        return (
            f"EMTPanel(id={self.id}, name={self.name!r}, "
            f"type=trackside/pitlane, active={self.active})"
        )