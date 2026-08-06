from structures.em_t_panel_custom_image import EMTPanelCustomImage
from services.logger import Logger

LOGO_TYPE = 0
SIGN_TYPE  = 1


class EMTPanelCustomImagesMapper:

    def _read_(self, old_cursor) -> list[EMTPanelCustomImage]:

        old_cursor.execute("SELECT * FROM t_custom_logos")
        logo_rows = old_cursor.fetchall()

        old_cursor.execute("SELECT * FROM t_custom_signs")
        sign_rows = old_cursor.fetchall()

        logo_count = len(logo_rows)
        result = []

        for row in logo_rows:
            c = EMTPanelCustomImage()
            c.id                    = row["ID"]
            c.name                  = row["Name"]
            c.source_file_extension = row["SourceFileExtension"]
            c.source_bitmap_md5     = row["SourceBitmapMd5Hash"]
            c.thumbnail_md5         = row["ThumbnailMd5Hash"]
            c.background_color      = row["BackgroundColor"]
            c.type                  = LOGO_TYPE
            result.append(c)

        for row in sign_rows:
            c = EMTPanelCustomImage()
            c.id                    = logo_count + row["ID"]
            c.name                  = row["Name"]
            c.source_file_extension = row["SourceFileExtension"]
            c.source_bitmap_md5     = row["SourceBitmapMd5Hash"]
            c.thumbnail_md5         = row["ThumbnailMd5Hash"]
            c.background_color      = row["BackgroundColor"]
            c.type                  = SIGN_TYPE
            result.append(c)

        return result

    def _write_(self, new_cursor, records: list[EMTPanelCustomImage]):
        new_cursor.execute("DELETE FROM t_em_t_panel_custom_images")
        new_cursor.executemany(
            "INSERT INTO t_em_t_panel_custom_images (ID, Name, SourceFileExtension, SourceBitmapMd5Hash, ThumbnailMd5Hash, BackgroundColor, Type) VALUES (?,?,?,?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_em_t_panel_custom_images")