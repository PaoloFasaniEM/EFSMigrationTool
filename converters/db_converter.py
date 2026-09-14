import os
import sqlite3

from converters.mappers.parameters_mapper import ParametersMapper
from converters.mappers.alkamel_timing_mapper import AlkamelTimingMapper
from converters.mappers.cars_mapper import CarsMapper
from converters.mappers.championships_mapper import ChampionshipsMapper
from converters.mappers.circuits_mapper import CircuitsMapper
from converters.mappers.circuit_disabled_rules_mapper import CircuitDisabledRulesMapper
from converters.mappers.circuit_alternative_rule_groups_mapper import CircuitAlternativeRuleGroupsMapper
from converters.mappers.circuit_panel_sets_mapper import CircuitPanelSetsMapper
from converters.mappers.circuit_panels_mapper import CircuitPanelsMapper
from converters.mappers.circuit_rule_sets_mapper import CircuitRuleSetsMapper
from converters.mappers.saved_rule_sets_mapper import SavedRuleSetsMapper
from converters.mappers.saved_rule_sets_alternative_groups_mapper import SavedRuleSetsAlternativeGroupsMapper
from converters.mappers.saved_rule_sets_disabled_mapper import SavedRuleSetsDisabledMapper
from converters.mappers.circuit_flag_frequencies_mapper import CircuitFlagFrequenciesMapper
from converters.mappers.circuit_flag_modes_mapper import CircuitFlagModesMapper
from converters.mappers.circuit_info_panel_penalty_rendering_mapper import CircuitInfoPanelPenaltyRenderingMapper
from converters.mappers.circuit_sectors_mapper import CircuitSectorsMapper
from converters.mappers.circuit_speed_limits_mapper import CircuitSpeedLimitsMapper
from converters.mappers.circuit_slow_down_zones_mapper import CircuitSlowDownZonesMapper
from converters.mappers.custom_images_mapper import CustomImagesMapper
from converters.mappers.em_t_panel_custom_images_mapper import EMTPanelCustomImagesMapper
from converters.mappers.em_info_panel_custom_images_mapper import EMInfoPanelCustomImagesMapper
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
        self.parameters_mapper                              = ParametersMapper()
        self.alkamel_timing_mapper                          = AlkamelTimingMapper()
        self.cars_mapper                                    = CarsMapper()
        self.championships_mapper                           = ChampionshipsMapper()
        self.circuits_mapper                                = CircuitsMapper()
        self.circuit_disabled_rules_mapper                  = CircuitDisabledRulesMapper()
        self.circuit_alternative_rule_groups_mapper         = CircuitAlternativeRuleGroupsMapper()
        self.circuit_panel_sets_mapper                      = CircuitPanelSetsMapper()
        self.circuit_panels_mapper                          = CircuitPanelsMapper()
        self.circuit_rule_sets_mapper                       = CircuitRuleSetsMapper()
        self.saved_rule_sets_mapper                         = SavedRuleSetsMapper()
        self.saved_rule_sets_alternative_groups_mapper      = SavedRuleSetsAlternativeGroupsMapper()
        self.saved_rule_sets_disabled_mapper                = SavedRuleSetsDisabledMapper()
        self.circuit_flag_frequencies_mapper                = CircuitFlagFrequenciesMapper()
        self.circuit_flag_modes_mapper                      = CircuitFlagModesMapper()
        self.circuit_info_panel_penalty_rendering_mapper    = CircuitInfoPanelPenaltyRenderingMapper()
        self.circuit_sectors_mapper                         = CircuitSectorsMapper()
        self.circuit_speed_limits_mapper                    = CircuitSpeedLimitsMapper()
        self.circuit_slow_down_zones_mapper                 = CircuitSlowDownZonesMapper()
        self.custom_images_mapper                           = CustomImagesMapper()
        self.em_t_panel_custom_images_mapper                = EMTPanelCustomImagesMapper()
        self.em_info_panel_custom_images_mapper             = EMInfoPanelCustomImagesMapper()
        self.ethernet_panels_mapper                         = EthernetPanelsMapper()
        self.saved_grid_countdowns_mapper                   = SavedGridCountdownsMapper()
        self.saved_messages_mapper                          = SavedMessagesMapper()
        self.saved_sessions_mapper                          = SavedSessionsMapper()
        self.session_manager_feeders_mapper                 = SessionManagerFeedersMapper()
        self.smart_marshalling_clients_mapper               = SmartMarshallingClientsMapper()
        self.starting_lights_control_units_mapper           = StartingLightsControlUnitsMapper()
        self.third_party_panels_servers_mapper              = ThirdPartyPanelsServersMapper()
        self.vic_flag_hex_codes_mapper                      = VICFlagHexCodesMapper()

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

        #t_parameters
        old_parameters = self.parameters_mapper._read_(old_cursor)
        self.parameters_mapper._write_(new_cursor, old_parameters)

        #t_alkamel_timing
        alkamel_timings = self.alkamel_timing_mapper._read_(old_cursor)
        self.alkamel_timing_mapper._write_(new_cursor, alkamel_timings)

        #t_cars
        cars = self.cars_mapper._read_(old_cursor)
        self.cars_mapper._write_(new_cursor, cars)

        #t_championships
        championships = self.championships_mapper._read_(old_cursor)
        self.championships_mapper._write_(new_cursor, championships)

        #t_circuits
        circuits = self.circuits_mapper._read_(old_cursor)
        self.circuits_mapper._write_(new_cursor, circuits)

        #t_circuit_alternative_rule_groups
        circuit_alternative_rule_groups = self.circuit_alternative_rule_groups_mapper._read_(old_cursor)
        self.circuit_alternative_rule_groups_mapper._write_(new_cursor, circuit_alternative_rule_groups)

        #t_circuit_disabled_rules
        circuit_disabled_rules = self.circuit_disabled_rules_mapper._read_(old_cursor)
        self.circuit_disabled_rules_mapper._write_(new_cursor, circuit_disabled_rules)

        #t_circuit_flag_frequencies
        circuit_flag_frequencies = self.circuit_flag_frequencies_mapper._read_(old_cursor)
        self.circuit_flag_frequencies_mapper._write_(new_cursor, circuit_flag_frequencies)

        #t_circuit_flag_modes
        circuit_flag_modes = self.circuit_flag_modes_mapper._read_(old_cursor)
        self.circuit_flag_modes_mapper._write_(new_cursor, circuit_flag_modes)

        #t_circuit_info_panel_penalty_rendering
        circuit_info_panel_penalty_rendering = self.circuit_info_panel_penalty_rendering_mapper._read_(old_cursor)
        self.circuit_info_panel_penalty_rendering_mapper._write_(new_cursor, circuit_info_panel_penalty_rendering)

        #t_circuit_panel_sets
        circuit_panel_sets = self.circuit_panel_sets_mapper._read_(old_cursor)
        self.circuit_panel_sets_mapper._write_(new_cursor, circuit_panel_sets)

        #t_circuit_panels
        circuit_panels = self.circuit_panels_mapper._read_(old_cursor)
        self.circuit_panels_mapper._write_(new_cursor, circuit_panels)

        #t_circuit_rule_sets
        circuit_rule_sets = self.circuit_rule_sets_mapper._read_(old_cursor)
        self.circuit_rule_sets_mapper._write_(new_cursor, circuit_rule_sets)

        #t_circuit_sectors
        circuit_sectors = self.circuit_sectors_mapper._read_(old_cursor)
        self.circuit_sectors_mapper._write_(new_cursor, circuit_sectors)

        #t_circuit_slow_down_zones
        circuit_slow_down_zones = self.circuit_slow_down_zones_mapper._read_(old_cursor)
        self.circuit_slow_down_zones_mapper._write_(new_cursor, circuit_slow_down_zones)

        #t_circuit_speed_limits
        circuit_speed_limits = self.circuit_speed_limits_mapper._read_(old_cursor)
        self.circuit_speed_limits_mapper._write_(new_cursor, circuit_speed_limits)

        #t_custom_images
        custom_images = self.custom_images_mapper._read_(old_cursor)
        self.custom_images_mapper._write_(new_cursor, custom_images)

        #t_em_info_panel_custom_images
        em_info_panel_custom_images = self.em_info_panel_custom_images_mapper._read_(old_cursor)
        self.em_info_panel_custom_images_mapper._write_(new_cursor, em_info_panel_custom_images)

        #t_em_t_panel_custom_images
        em_t_panel_custom_images = self.em_t_panel_custom_images_mapper._read_(old_cursor)
        self.em_t_panel_custom_images_mapper._write_(new_cursor, em_t_panel_custom_images)

        #t_em_t_panels + t_em_info_panels + t_third_party_panels
        t_panels, info_panels, third_party = self.ethernet_panels_mapper._read_(old_cursor)
        self.ethernet_panels_mapper._write_(new_cursor, t_panels, info_panels, third_party)

        #t_saved_grid_countdowns
        saved_grid_countdowns = self.saved_grid_countdowns_mapper._read_(old_cursor)
        self.saved_grid_countdowns_mapper._write_(new_cursor, saved_grid_countdowns)

        #t_saved_messages
        saved_messages = self.saved_messages_mapper._read_(old_cursor)
        self.saved_messages_mapper._write_(new_cursor, saved_messages)

        #t_saved_rule_sets
        saved_rule_sets = self.saved_rule_sets_mapper._read_(old_cursor)
        self.saved_rule_sets_mapper._write_(new_cursor, saved_rule_sets)

        #t_saved_rule_sets_alternative_groups
        saved_rule_sets_alternative_groups = self.saved_rule_sets_alternative_groups_mapper._read_(old_cursor)
        self.saved_rule_sets_alternative_groups_mapper._write_(new_cursor, saved_rule_sets_alternative_groups)

        #t_saved_rule_sets_disabled
        saved_rule_sets_disabled = self.saved_rule_sets_disabled_mapper._read_(old_cursor)
        self.saved_rule_sets_disabled_mapper._write_(new_cursor, saved_rule_sets_disabled)

        #t_saved_sessions
        saved_sessions = self.saved_sessions_mapper._read_(old_cursor)
        self.saved_sessions_mapper._write_(new_cursor, saved_sessions)

        #t_session_manager_feeders
        session_manager_feeders = self.session_manager_feeders_mapper._read_(old_cursor)
        self.session_manager_feeders_mapper._write_(new_cursor, session_manager_feeders)

        #t_smart_marshalling_clients
        smart_marshalling_clients = self.smart_marshalling_clients_mapper._read_(old_cursor)
        self.smart_marshalling_clients_mapper._write_(new_cursor, smart_marshalling_clients)

        #t_starting_lights_control_units + t_third_party_scus
        scus, third_party_scus = self.starting_lights_control_units_mapper._read_(old_cursor)
        self.starting_lights_control_units_mapper._write_(new_cursor, scus, third_party_scus)

        #t_third_party_panels_servers
        third_party_panels_servers = self.third_party_panels_servers_mapper._read_(old_cursor)
        self.third_party_panels_servers_mapper._write_(new_cursor, third_party_panels_servers)

        #t_vic_flag_hex_codes
        vic_flag_hex_codes = self.vic_flag_hex_codes_mapper._read_(old_cursor)
        self.vic_flag_hex_codes_mapper._write_(new_cursor, vic_flag_hex_codes)