import os
import shutil
import sqlite3
from services.logger import Logger

class MapsConverter:

    def convert(self, old_path: str, new_path: str):

        old_db_path = os.path.join(old_path, "EFS.Server.db")

        old_maps_dir = os.path.join(old_path, "maps")
        old_sm_maps_dir = os.path.join(old_path, "smMaps")

        new_maps_root = os.path.join(new_path, "maps")

        if not os.path.exists(old_db_path):
            raise FileNotFoundError(f"Missing DB: {old_db_path}")

        if not os.path.exists(old_maps_dir):
            raise FileNotFoundError(f"Missing folder: {old_maps_dir}")

        if not os.path.exists(old_sm_maps_dir):
            raise FileNotFoundError(f"Missing folder: {old_sm_maps_dir}")

        os.makedirs(new_maps_root, exist_ok=True)

        conn = sqlite3.connect(old_db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT ID, Name, MapFile, SMMapFile
            FROM t_maps
        """)

        rows = cursor.fetchall()
        conn.close()

        copied = 0

        for row in rows:

            circuit_id = str(row["ID"])
            circuit_name = row["Name"] if row["Name"] else f"Circuit {circuit_id}"
            map_file = row["MapFile"]
            sm_map_file = row["SMMapFile"]

            target_dir = os.path.join(new_maps_root, circuit_id)
            os.makedirs(target_dir, exist_ok=True)

            map_copied    = False
            sm_map_copied = False

            # MAP
            if map_file:
                map_copied = self._copy_file(
                    os.path.join(old_maps_dir, map_file),
                    os.path.join(target_dir, map_file)
                )

            # CMAP
            if sm_map_file:
                sm_map_copied = self._copy_file(
                    os.path.join(old_sm_maps_dir, sm_map_file),
                    os.path.join(target_dir, sm_map_file)
                )

            if map_copied and sm_map_copied:
                Logger.ok(f"{circuit_name}: map and SM map copied")
            elif map_copied:
                Logger.warn(f"{circuit_name}: only map copied, SM map missing")
            elif sm_map_copied:
                Logger.warn(f"{circuit_name}: only SM map copied, map missing")
            else:
                Logger.warn(f"{circuit_name}: no files copied")

            copied += 1

        Logger.info(f"Processed {copied} circuits")

    def _copy_file(self, src, dst) -> bool:
        if not os.path.exists(src):
            Logger.warn(f"Missing file: {src}")
            return False

        shutil.copy2(src, dst)
        return True