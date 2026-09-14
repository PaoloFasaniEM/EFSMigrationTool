from converters.db_converter import DbConverter
from converters.folders_converter import FoldersConverter
from converters.maps_converter import MapsConverter
from converters.custom_images_converter import CustomImagesConverter
from services.logger import Logger



class MigrationService:

    def __init__(self):
        self.db_converter = DbConverter()
        self.folders_converter = FoldersConverter()
        self.maps_converter = MapsConverter()
        self.custom_images_converter = CustomImagesConverter()

    def import_all(self, old_path, new_path, copy_sessions=False, copy_journal=False):

        Logger.info("Starting import process...")

        try:

            try:
                Logger.info("Converting database...")
                self.db_converter.convert(old_path, new_path)
                Logger.ok("Database conversion completed")
            except Exception as ex:
                Logger.error(f"Database conversion failed: {ex}")
                Logger.error("Import aborted.")
                return

            try:
                Logger.info("Converting track maps...")
                self.maps_converter.convert(old_path, new_path)
                Logger.ok("Track maps conversion completed")
            except Exception as ex:
                Logger.error(f"Track maps conversion failed: {ex}")

            try:
                Logger.info("Converting images...")
                self.custom_images_converter.convert(old_path, new_path)
                Logger.ok("Images conversion completed")
            except Exception as ex:
                Logger.error(f"Images conversion failed: {ex}")

            if copy_sessions:
                self.copy_folder(old_path, new_path, "sessions")

            if copy_journal:
                self.copy_folder(old_path, new_path, "journal")

            Logger.ok("Import completed")

        except Exception as ex:
            Logger.error(str(ex))

    def copy_folder(self, old_path, new_path, folder_name):
        Logger.info(f"Copying {folder_name}...")
        self.folders_converter.convert_single(old_path, new_path, folder_name)
        Logger.ok(f"{folder_name.capitalize()} copy completed")