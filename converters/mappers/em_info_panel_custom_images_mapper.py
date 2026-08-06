from structures.em_info_panel_custom_image import EMInfoPanelCustomImage
from services.logger import Logger

LOGO_TYPE = 0


class EMInfoPanelCustomImagesMapper:

    def _read_(self, old_cursor) -> list[EMInfoPanelCustomImage]:

        old_cursor.execute("SELECT * FROM t_custom_logos")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_custom_logos for info panel")

        result = []

        for row in rows:
            has_info_source = bool(row["InfoPanelSourceBitmapMd5Hash"])

            c = EMInfoPanelCustomImage()
            c.id               = row["ID"]
            c.name             = row["Name"]
            c.background_color = row["BackgroundColor"]
            c.type             = LOGO_TYPE

            if has_info_source:
                c.source_file_extension = row["InfoPanelSourceFileExtension"]
                c.source_bitmap_md5     = row["InfoPanelSourceBitmapMd5Hash"]
            else:
                c.source_file_extension = row["SourceFileExtension"]
                c.source_bitmap_md5     = row["SourceBitmapMd5Hash"]

            c.thumbnail_md5 = row["ThumbnailMd5Hash"]
            result.append(c)

        return result

    def _write_(self, new_cursor, records: list[EMInfoPanelCustomImage]):
        new_cursor.execute("DELETE FROM t_em_info_panel_custom_images")
        new_cursor.executemany(
            "INSERT INTO t_em_info_panel_custom_images (ID, Name, SourceFileExtension, SourceBitmapMd5Hash, ThumbnailMd5Hash, BackgroundColor, Type) VALUES (?,?,?,?,?,?,?)",
            [r.to_db_tuple() for r in records]
        )
        Logger.ok(f"Written {len(records)} records to t_em_info_panel_custom_images")