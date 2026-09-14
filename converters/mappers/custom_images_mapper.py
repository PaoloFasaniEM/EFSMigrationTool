from structures.custom_image import CustomImage
from utils.flag_converter import int_to_rrggbb
from services.logger import Logger
from utils.db_utils import safe_int

LOGO_TYPE = 0
SIGN_TYPE  = 1


class CustomImagesMapper:

    def _read_(self, old_cursor) -> list[CustomImage]:

        old_cursor.execute("SELECT * FROM t_custom_logos")
        logo_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(logo_rows)} records in t_custom_logos")

        old_cursor.execute("SELECT * FROM t_custom_signs")
        sign_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(sign_rows)} records in t_custom_signs")

        logo_count = len(logo_rows)
        result = []

        for row in logo_rows:
            c = CustomImage()
            c.id               = row["ID"]
            c.name             = row["Name"]
            c.background_color = int_to_rrggbb(safe_int(row["BackgroundColor"]))
            c.type             = LOGO_TYPE
            result.append(c)

        for row in sign_rows:
            c = CustomImage()
            c.id               = logo_count + row["ID"]
            c.name             = row["Name"]
            c.background_color = int_to_rrggbb(safe_int(row["BackgroundColor"]))
            c.type             = SIGN_TYPE
            result.append(c)

        return result

    def _write_(self, new_cursor, records: list[CustomImage]):
        new_cursor.execute("DELETE FROM t_custom_images")
        new_cursor.executemany(
            "INSERT INTO t_custom_images (ID, Name, BackgroundColor, Type) VALUES (?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_custom_images")