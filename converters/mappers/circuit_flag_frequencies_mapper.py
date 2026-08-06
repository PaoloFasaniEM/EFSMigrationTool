# converters/mappers/circuit_flag_frequencies_mapper.py

from structures.circuit_flag_frequency import CircuitFlagFrequency
from utils.flag_converter import convert_flag
from services.logger import Logger


class CircuitFlagFrequenciesMapper:

    def _read_(self, old_cursor) -> list[CircuitFlagFrequency]:

        old_cursor.execute("SELECT * FROM t_flag_frequencies")
        freq_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(freq_rows)} records in t_flag_frequencies")

        old_cursor.execute("SELECT * FROM t_silent_flags")
        silent_rows = old_cursor.fetchall()
        Logger.info(f"Found {len(silent_rows)} records in t_silent_flags")

        silent_set: set[tuple] = {
            (row["MapId"], int(row["Flag"])) for row in silent_rows
        }

        result = []

        for row in freq_rows:
            old_flag   = int(row["Flag"])
            circuit_id = row["MapId"]
            new_flag   = convert_flag(old_flag)

            if new_flag is None:
                Logger.warn(f"No mapping for old flag {old_flag}, skipping")
                continue

            f = CircuitFlagFrequency()
            f.id         = int(new_flag)
            f.circuit_id = circuit_id
            f.frequency  = row["Frequency"]
            f.silent     = 1 if (circuit_id, old_flag) in silent_set else 0

            result.append(f)

        Logger.info(f"Composed {len(result)} circuit flag frequencies")
        return result

    def _write_(self, new_cursor, frequencies: list[CircuitFlagFrequency]):

        new_cursor.execute("DELETE FROM t_circuit_flag_frequencies")

        sql = """
            INSERT INTO t_circuit_flag_frequencies (
                ID, CircuitID, Frequency, Silent
            ) VALUES (?,?,?,?)
        """

        new_cursor.executemany(sql, [f.to_db_tuple() for f in frequencies])
        Logger.ok(f"Written {len(frequencies)} records to t_circuit_flag_frequencies")