def safe_int(value, default: int = 0) -> int:
    if value is None or str(value).strip() == "":
        return default
    return int(value)