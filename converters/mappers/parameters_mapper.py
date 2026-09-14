# converters/mappers/parameters_mapper.py

from services.logger import Logger


class ParametersMapper:

    def _read_(self, old_cursor) -> dict[tuple, str]:
        old_cursor.execute("SELECT * FROM t_parameters")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_parameters")

        return {
            (row["ParameterGroup"], row["ParameterName"]): row["ParameterValue"]
            for row in rows
        }

    def _write_(self, new_cursor, old: dict[tuple, str]):

        def get(group: str, name: str) -> str:
            return old.get((group, name), "")

        def get_ms(group: str, name: str) -> str:
            val = get(group, name)
            if val == "":
                return ""
            return str(int(val) * 1000)

        mappings: list[tuple[str, str, str]] = [

            # TimingServerSessions
            ("TimingServerSessions", "ShowLapsAndRunningTimeEnabled",    get("Server", "TimingServerSessionsShowLapsAndRunningTimeEnabled")),
            ("TimingServerSessions", "SessionRecordingEnabled",          get("Server", "TimingServerSessionsSessionRecordingEnabled")),
            ("TimingServerSessions", "AllowSessionSuspensionEnabled",    get("Server", "TimingServerAllowSessionSuspensionEnabled")),

            # Connection
            ("Connection", "AutoconnectAtStartup",              get("PanelConnections", "AutoconnectAtStartup")),
            ("Connection", "UsePanels",                         get("PanelConnections", "UseTrackPanels")),
            ("Connection", "UseCars",                           get("PanelConnections", "UseCarEquipments")),
            ("Connection", "UseStartingLightsControlUnits",     get("PanelConnections", "UseStartingLightsControlUnits")),
            ("Connection", "UseTimingServers",                  get("PanelConnections", "UseTimingServers")),
            ("Connection", "UseThirdPartyPanels",               get("PanelConnections", "UseThirdPartyPanels")),

            # Clients
            ("Clients", "ListeningPort",            get("Server", "ListeningPort")),
            ("Clients", "StartListeningAtStartup",  get("Server", "StartListenAtStartup")),
            ("Clients", "CircuitRefreshTime",        get("Server", "ClientCircuitRefreshTime")),
            ("Clients", "CarsRefreshTime",           get("Server", "ClientCarsRefreshTime")),

            # AutomaticOperator
            ("AutomaticOperator", "Enabled", get("AutomaticOperator", "Enabled")),

            # SessionRecording
            ("SessionRecording", "EnableRecording",        get("DumpOptions", "EnableSessionDataRecording")),
            ("SessionRecording", "MaxRecordingFileSizeMB", get("DumpOptions", "SessionDataFileMaxSizeMB")),

            # EMTPanels
            ("EMTPanels", "EnableDump",              get("DumpOptions", "EnablePanelsDump")),
            ("EMTPanels", "MaxDumpFileSizeMB",       get("DumpOptions", "PanelsDumpMaxSize")),
            ("EMTPanels", "StatusRefreshTime",       get("EthernetConnectionSettings", "AesysStatusRefreshTime")),
            ("EMTPanels", "TxTimeout",               get("EthernetConnectionSettings", "AesysTxTimeout")),
            ("EMTPanels", "UploadTimeout",           get("EthernetConnectionSettings", "AesysUploadTimeout")),
            ("EMTPanels", "PacketSenderAddress",     get("EthernetConnectionSettings", "AesysPacketSenderAddress")),
            ("EMTPanels", "ConsoleCurrentTimeMaxDelay", get("EthernetConnectionSettings", "AesysConsoleCurrentTimeMaxDelay")),

            # EMInfoPanels
            ("EMInfoPanels", "EnableDump",        get("DumpOptions", "EnablePanelsDump")),
            ("EMInfoPanels", "MaxDumpFileSizeMB", get("DumpOptions", "PanelsDumpMaxSize")),
            ("EMInfoPanels", "StatusRefreshTime", get("EthernetConnectionSettings", "EMLiveBoardStatusRefreshTime")),
            ("EMInfoPanels", "TxTimeout",         get("EthernetConnectionSettings", "EMLiveBoardTxTimeout")),
            ("EMInfoPanels", "SyncDelta",         get("EthernetConnectionSettings", "EMLiveBoardSyncDelta")),

            # EMStartingGridPanels
            ("EMStartingGridPanels", "EnableDump",        get("DumpOptions", "EnablePanelsDump")),
            ("EMStartingGridPanels", "MaxDumpFileSizeMB", get("DumpOptions", "PanelsDumpMaxSize")),

            # ExternalPanelManager
            ("ExternalPanelManager", "Port",                 get("ExternalPanelManager", "Port")),
            ("ExternalPanelManager", "StatusRefreshMs",      get("ExternalPanelManager", "StatusRefreshMs")),
            ("ExternalPanelManager", "StartListenAtStartup", get("ExternalPanelManager", "StartListenAtStartup")),
            ("ExternalPanelManager", "EnableDump",           get("DumpOptions", "EnableEpmDump")),
            ("ExternalPanelManager", "MaxDumpFileSizeMB",    get("DumpOptions", "EpmDumpMaxSize")),

            # XmlPermissions
            ("XmlPermissions", "Configuration",         get("XmlPermissions", "Configuration")),
            ("XmlPermissions", "Heartbeat",             get("XmlPermissions", "Heartbeat")),
            ("XmlPermissions", "TrackStatus",           get("XmlPermissions", "TrackStatus")),
            ("XmlPermissions", "SectorsStatus",         get("XmlPermissions", "SectorsStatus")),
            ("XmlPermissions", "PenaltyFlags",          get("XmlPermissions", "PenaltyFlags")),
            ("XmlPermissions", "CircuitMessages",       get("XmlPermissions", "CircuitMessages")),
            ("XmlPermissions", "StartingLightsStatus",  get("XmlPermissions", "StartingLightsStatus")),
            ("XmlPermissions", "CountStatus",           get("XmlPermissions", "CountStatus")),
            ("XmlPermissions", "Diagnostics",           get("XmlPermissions", "Diagnostics")),
            ("XmlPermissions", "SetTrack",              get("XmlPermissions", "SetTrack")),
            ("XmlPermissions", "SetSectors",            get("XmlPermissions", "SetSectors")),
            ("XmlPermissions", "SetPenaltyFlags",       get("XmlPermissions", "SetPenaltyFlags")),
            ("XmlPermissions", "SetCircuitMessages",    get("XmlPermissions", "SetCircuitMessages")),
            ("XmlPermissions", "SetStartingLights",     get("XmlPermissions", "SetStartingLights")),
            ("XmlPermissions", "SetCount",              get("XmlPermissions", "SetCount")),
            ("XmlPermissions", "SetPanelFlags",         get("XmlPermissions", "SetPanelFlags")),

            # SessionManagerFeeders
            ("SessionManagerFeeders", "HeartbeatTimeoutMs",            get("SessionManager", "HeartbeatTimeout")),
            ("SessionManagerFeeders", "LoginFailedReconnectTimeoutMs", get("SessionManager", "LoginFailedTimeout")),

            # SmartMarshallingClients
            ("SmartMarshallingClients", "LoginFailedReconnectTimeoutMs", get("SmartMarshalling", "LoginFailedTimeout")),

            # ThirdPartyPanels
            ("ThirdPartyPanels", "LoginFailedReconnectTimeoutMs", get("ThirdPartyPanels", "LoginFailedTimeout")),
            ("ThirdPartyPanels", "EnableDump",                    get("DumpOptions", "EnableTppDump")),
            ("ThirdPartyPanels", "MaxDumpFileSizeMB",             get("DumpOptions", "TppDumpMaxSize")),

            # Cars
            ("Cars", "FollowOnTrackMaxPacketLostDelayMs",      get("EFSCarsUSB", "FollowOnTrackMaxPacketLostDelayMs")),
            ("Cars", "EquipmentOffTimeoutMs",                  get_ms("CarRuntimeParameters", "EquipmentOffTimeout")),
            ("Cars", "CarParkedTimeoutMs",                     get_ms("CarRuntimeParameters", "CarParkedTimeout")),
            ("Cars", "MaxDistanceDelta",                       get("CarRuntimeParameters", "MaxDistanceDelta")),
            ("Cars", "AccidentAlertEnabled",                   get("CarRuntimeParameters", "AccidentAlertEnabled")),
            ("Cars", "AccidentAlertThreshold",                 get("CarRuntimeParameters", "AccidentAlertThresholdEdit")),
            ("Cars", "HighThresholdDeltaMs",                   get_ms("CarRuntimeParameters", "HighThresholdDelta")),
            ("Cars", "HighThresholdSpeed",                     get("CarRuntimeParameters", "HighThresholdSpeed")),
            ("Cars", "LowThresholdDeltaMs",                    get_ms("CarRuntimeParameters", "LowThresholdDelta")),
            ("Cars", "LowThresholdSpeed",                      get("CarRuntimeParameters", "LowThresholdSpeed")),
            ("Cars", "RaceCarCoverageThresholdSpeed",          get("CarRuntimeParameters", "RaceCarCoverageThresholdSpeed")),
            ("Cars", "ServiceVehicleCoverageThresholdSpeed",   get("CarRuntimeParameters", "ServiceVehicleCoverageThresholdSpeed")),
            ("Cars", "CoverageThresholdDeltaMs",               get_ms("CarRuntimeParameters", "CoverageThresholdDelta")),

            # Location
            ("Location", "CountryCode",   get("Location", "CountryCode")),
            ("Location", "NormLatitude",  get("Location", "NormLatitude")),
            ("Location", "NormLongitude", get("Location", "NormLongitude")),
            ("Location", "Place",         get("Location", "Place")),
        ]

        for group, name, value in mappings:
            new_cursor.execute(
                "UPDATE t_parameters SET ParameterValue = ? WHERE ParameterGroup = ? AND ParameterName = ?",
                (value, group, name)
            )

        Logger.ok(f"Updated {len(mappings)} parameters")