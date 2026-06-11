import os
import sqlite3

from converters.mappers.alkamel_timing_mapper import AlkamelTimingMapper
from converters.mappers.circuits_mapper import CircuitsMapper
from converters.mappers.ethernet_panels_mapper import EthernetPanelsMapper
from converters.mappers.smart_marshalling_clients_mapper import SmartMarshallingClientsMapper
from converters.mappers.vic_flag_hex_codes_mapper import VICFlagHexCodesMapper
from services.logger import Logger

class DbConverter:

    def __init__(self):
        self.alkamel_timing_mapper              = AlkamelTimingMapper()
        self.circuits_mapper                    = CircuitsMapper()
        self.ethernet_panels_mapper             = EthernetPanelsMapper()
        self.smart_marshalling_clients_mapper   = SmartMarshallingClientsMapper()
        self.vic_flag_hex_codes_mapper          = VICFlagHexCodesMapper()

    def convert(self, old_path, new_path):

        old_db_path = os.path.join(old_path, "EFS.Server.db")
        new_db_path = os.path.join(new_path, "EMElectronicFlagsServer.Service.db")

        if not os.path.exists(old_db_path):
            raise FileNotFoundError(f"Old database not found: {old_db_path}")

        if not os.path.exists(new_db_path):
            raise FileNotFoundError(f"New database not found: {new_db_path}")

        old_conn = None
        new_conn = None

        try:
            old_conn = sqlite3.connect(old_db_path)
            old_conn.row_factory = sqlite3.Row

            new_conn = sqlite3.connect(new_db_path)

            old_cursor = old_conn.cursor()
            new_cursor = new_conn.cursor()

            self._convert_all_tables(old_cursor, new_cursor)

            new_conn.commit()
            return True

        except sqlite3.Error as e:
            Logger.error(f"[DB ERROR] {e}")
            return False

        finally:
            if old_conn:
                old_conn.close()
            if new_conn:
                new_conn.close()



    def _convert_all_tables(self, old_cursor, new_cursor):

            #t_alkamel_timing
            alkamel_timings = self.alkamel_timing_mapper._read_(old_cursor)
            self.alkamel_timing_mapper._write_(new_cursor, alkamel_timings)

            #t_circuits
            circuits = self.circuits_mapper._read_(old_cursor)
            self.circuits_mapper._write_(new_cursor, circuits)

            #t_ethernet_panels
            t_panels, info_panels, third_party = self.ethernet_panels_mapper._read_(old_cursor)
            self.ethernet_panels_mapper._write_(new_cursor, t_panels, info_panels, third_party)

            #t_smart_marshalling_clients
            smart_marshalling_clients = self.smart_marshalling_clients_mapper._read_(old_cursor)
            self.smart_marshalling_clients_mapper._write_(new_cursor, smart_marshalling_clients)

            #t_vic_flag_hex_codes
            vic_flag_hex_codes = self.vic_flag_hex_codes_mapper._read_(old_cursor)
            self.vic_flag_hex_codes_mapper._write_(new_cursor, vic_flag_hex_codes)