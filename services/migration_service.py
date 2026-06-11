from converters.db_converter import DbConverter
from converters.maps_converter import MapsConverter
from services.logger import Logger


class MigrationService:

    def __init__(self):
        self.db_converter = DbConverter()
        self.maps_converter = MapsConverter()

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
            # image_converter.convert(...)
            Logger.ok("Images conversion completed")

            Logger.ok("Import completed")

        except Exception as ex:
            Logger.error(str(ex))