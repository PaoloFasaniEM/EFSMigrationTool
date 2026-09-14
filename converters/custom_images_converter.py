# converters/custom_images_converter.py

import os
import shutil
import sqlite3
from services.logger import Logger


class CustomImagesConverter:

    def convert(self, old_path: str, new_path: str):

        old_db_path = os.path.join(old_path, "EFS.Server.db")

        old_logo_dir = os.path.join(old_path, "custom", "logo")
        old_sign_dir = os.path.join(old_path, "custom", "sign")

        new_emt_dir = os.path.join(new_path, "custom", "EMTPanel", "customImages")
        new_emi_dir = os.path.join(new_path, "custom", "EMInfoPanel", "customImages")

        if not os.path.exists(old_db_path):
            raise FileNotFoundError(f"Missing DB: {old_db_path}")

        if not os.path.exists(old_logo_dir):
            Logger.warn(f"Logo folder missing, skipping custom images: {old_logo_dir}")
            return

        if not os.path.exists(old_sign_dir):
            Logger.warn(f"Sign folder missing, skipping custom images: {old_sign_dir}")
            return

        os.makedirs(new_emt_dir, exist_ok=True)
        os.makedirs(new_emi_dir, exist_ok=True)

        conn = sqlite3.connect(old_db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT ID, Name, InfoPanelSourceBitmapMd5Hash, SourceFileExtension, InfoPanelSourceFileExtension FROM t_custom_logos")
        logo_rows = cursor.fetchall()

        cursor.execute("SELECT ID, Name, SourceFileExtension FROM t_custom_signs")
        sign_rows = cursor.fetchall()

        conn.close()

        logo_count = len(logo_rows)

        #LOGO
        for row in logo_rows:
            logo_id  = row["ID"]
            new_id   = logo_id
            has_info = bool(row["InfoPanelSourceBitmapMd5Hash"])

            ext      = row["SourceFileExtension"]
            info_ext = row["InfoPanelSourceFileExtension"] if has_info else ext

            old_t_source    = os.path.join(old_logo_dir, str(logo_id), f"Logo_{logo_id}_Source.{ext}")
            old_info_source = os.path.join(old_logo_dir, str(logo_id), f"Logo_{logo_id}_InfoPanelSource.{info_ext}")

            new_emt_target_dir = os.path.join(new_emt_dir, str(new_id))
            new_emi_target_dir = os.path.join(new_emi_dir, str(new_id))

            os.makedirs(new_emt_target_dir, exist_ok=True)
            os.makedirs(new_emi_target_dir, exist_ok=True)

            new_emt_source = os.path.join(new_emt_target_dir, f"Image_{new_id}_Source.{ext}")
            new_emi_source = os.path.join(new_emi_target_dir, f"Image_{new_id}_Source.{info_ext}")

            # T-panel source
            ok = self._copy_file(old_t_source, new_emt_source)
            if ok:
                Logger.ok(f"Logo {logo_id}: T-panel source copied")

            # Info panel source: usa InfoPanelSource se esiste, altrimenti fallback a T-panel
            if has_info:
                ok = self._copy_file(old_info_source, new_emi_source)
                if ok:
                    Logger.ok(f"Logo {logo_id}: info panel source copied")
            else:
                ok = self._copy_file(old_t_source, new_emi_source)
                if ok:
                    Logger.ok(f"Logo {logo_id}: info panel source copied (fallback from T-panel)")

        #SIGN
        for row in sign_rows:
            sign_id = row["ID"]
            new_id  = logo_count + sign_id

            ext = row["SourceFileExtension"]

            old_source     = os.path.join(old_sign_dir, str(sign_id), f"Sign_{sign_id}_Source.{ext}")

            new_emt_target_dir = os.path.join(new_emt_dir, str(new_id))
            os.makedirs(new_emt_target_dir, exist_ok=True)

            new_emt_source = os.path.join(new_emt_target_dir, f"Image_{new_id}_Source.{ext}")

            ok = self._copy_file(old_source, new_emt_source)
            if ok:
                Logger.ok(f"Sign {sign_id} -> Image {new_id}: T-panel source copied")

        Logger.info(f"Processed {len(logo_rows)} logos and {len(sign_rows)} signs")

    def _copy_file(self, src: str, dst: str) -> bool:
        if not os.path.exists(src):
            Logger.warn(f"Missing file: {src}")
            return False
        shutil.copy2(src, dst)
        return True