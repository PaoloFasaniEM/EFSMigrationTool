import os
import shutil
from services.logger import Logger


class FoldersConverter:

    def convert_single(self, old_path: str, new_path: str, folder: str):
        src = os.path.join(old_path, folder)
        dst = os.path.join(new_path, folder)

        if not os.path.exists(src):
            Logger.warn(f"Missing folder: {src}")
            return

        if os.path.exists(dst):
            shutil.rmtree(dst)

        shutil.copytree(src, dst)
        Logger.ok(f"Folder '{folder}' copied")