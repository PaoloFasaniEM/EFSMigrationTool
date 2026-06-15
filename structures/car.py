class Car:

    def __init__(self):
        self.id:                        int | None = None
        self.type:                      int | None = None
        self.active:                    int | None = None
        self.circuit_number:            int | None = None
        self.number:                    int | None = None
        self.label:                     str | None = None
        self.all_championship_allowed:  int | None = None
        self.championship_name:         str | None = None
        self.fixed_circuit_number:      int | None = None
        self.default_circuit_number:    int | None = None

    def to_db_tuple(self):
        return (
            self.id,
            self.type,
            self.active,
            self.circuit_number,
            self.number,
            self.label,
            self.all_championship_allowed,
            self.championship_name,
            self.fixed_circuit_number,
            self.default_circuit_number,
        )

    def __repr__(self):
        return (
            f"Car(id={self.id}, number={self.number}, "
            f"type={self.type}, active={self.active})"
        )