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

    def import_all(self, old_path, new_path):

        Logger.info("Starting import process...")

        try:

            Logger.info("Converting database...")
            self.db_converter.convert(old_path, new_path)
            Logger.ok("Database conversion completed")

            Logger.info("Converting track maps...")
            self.maps_converter.convert(old_path, new_path)
            Logger.ok("Track maps conversion completed")

            Logger.info("Converting images...")
            self.custom_images_converter.convert(old_path, new_path)
            Logger.ok("Images conversion completed")

            Logger.info("Copying folders...")
            self.folders_converter.convert(old_path, new_path)
            Logger.ok("Folders copy completed")

            Logger.ok("Import completed")

        except Exception as ex:
            Logger.error(str(ex))