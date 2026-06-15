import os
import sqlite3

from converters.mappers.alkamel_timing_mapper import AlkamelTimingMapper
from converters.mappers.cars_mapper import CarsMapper
from converters.mappers.circuits_mapper import CircuitsMapper
from converters.mappers.circuit_slow_down_zones_mapper import CircuitSlowDownZonesMapper
from converters.mappers.ethernet_panels_mapper import EthernetPanelsMapper
from converters.mappers.saved_grid_countdowns_mapper import SavedGridCountdownsMapper
from converters.mappers.saved_messages_mapper import SavedMessagesMapper
from converters.mappers.saved_sessions_mapper import SavedSessionsMapper
from converters.mappers.session_manager_feeders_mapper import SessionManagerFeedersMapper
from converters.mappers.smart_marshalling_clients_mapper import SmartMarshallingClientsMapper
from converters.mappers.starting_lights_control_units_mapper import StartingLightsControlUnitsMapper
from converters.mappers.third_party_panels_servers_mapper import ThirdPartyPanelsServersMapper
from converters.mappers.vic_flag_hex_codes_mapper import VICFlagHexCodesMapper
from services.logger import Logger

class DbConverter:

    def __init__(self):
        self.alkamel_timing_mapper                  = AlkamelTimingMapper()
        self.cars_mapper                            = CarsMapper()
        self.circuits_mapper                        = CircuitsMapper()
        self.circuit_slow_down_zones_mapper         = CircuitSlowDownZonesMapper()
        self.ethernet_panels_mapper                 = EthernetPanelsMapper()
        self.saved_grid_countdowns_mapper           = SavedGridCountdownsMapper()
        self.saved_messages_mapper                  = SavedMessagesMapper()
        self.saved_sessions_mapper                  = SavedSessionsMapper()
        self.session_manager_feeders_mapper         = SessionManagerFeedersMapper()
        self.smart_marshalling_clients_mapper       = SmartMarshallingClientsMapper()
        self.starting_lights_control_units_mapper   = StartingLightsControlUnitsMapper()
        self.third_party_panels_servers_mapper      = ThirdPartyPanelsServersMapper()
        self.vic_flag_hex_codes_mapper              = VICFlagHexCodesMapper()

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

            #t_cars
            cars = self.cars_mapper._read_(old_cursor)
            self.cars_mapper._write_(new_cursor, cars)
            
            #t_circuits
            circuits = self.circuits_mapper._read_(old_cursor)
            self.circuits_mapper._write_(new_cursor, circuits)

            #t_slow_zones
            circuit_slow_down_zones = self.circuit_slow_down_zones_mapper._read_(old_cursor)
            self.circuit_slow_down_zones_mapper._write_(new_cursor, circuit_slow_down_zones)

            #t_ethernet_panels
            t_panels, info_panels, third_party = self.ethernet_panels_mapper._read_(old_cursor)
            self.ethernet_panels_mapper._write_(new_cursor, t_panels, info_panels, third_party)

            #t_saved_grid_countdowns
            saved_grid_countdowns = self.saved_grid_countdowns_mapper._read_(old_cursor)
            self.saved_grid_countdowns_mapper._write_(new_cursor, saved_grid_countdowns)

            #t_saved_messages
            saved_messages = self.saved_messages_mapper._read_(old_cursor)
            self.saved_messages_mapper._write_(new_cursor, saved_messages)

            #t_saved_sessions
            saved_sessions = self.saved_sessions_mapper._read_(old_cursor)
            self.saved_sessions_mapper._write_(new_cursor, saved_sessions)

            #t_session_manager_feeders
            session_manager_feeders = self.session_manager_feeders_mapper._read_(old_cursor)
            self.session_manager_feeders_mapper._write_(new_cursor, session_manager_feeders)

            #t_smart_marshalling_clients
            smart_marshalling_clients = self.smart_marshalling_clients_mapper._read_(old_cursor)
            self.smart_marshalling_clients_mapper._write_(new_cursor, smart_marshalling_clients)

            #t_starting_light_control_units
            scus, third_party_scus = self.starting_lights_control_units_mapper._read_(old_cursor)
            self.starting_lights_control_units_mapper._write_(new_cursor, scus, third_party_scus)

            #t_third_party_panels_servers
            third_party_panels_servers = self.third_party_panels_servers_mapper._read_(old_cursor)
            self.third_party_panels_servers_mapper._write_(new_cursor, third_party_panels_servers)

            #t_vic_flag_hex_codes
            vic_flag_hex_codes = self.vic_flag_hex_codes_mapper._read_(old_cursor)
            self.vic_flag_hex_codes_mapper._write_(new_cursor, vic_flag_hex_codes)