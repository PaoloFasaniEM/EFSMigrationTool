from structures.circuit_speed_limit import CircuitSpeedLimit
from utils.flag_converter import convert_speed_limit_flag
from services.logger import Logger


class CircuitSpeedLimitsMapper:

    def _read_(self, old_cursor) -> list[CircuitSpeedLimit]:

        old_cursor.execute("SELECT * FROM t_speed_limits")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_speed_limits")

        result = []

        for row in rows:
            old_flag   = int(row["Flag"])
            new_flag   = convert_speed_limit_flag(old_flag)

            if new_flag is None:
                Logger.warn(f"No mapping for speed limit flag {old_flag}, skipping")
                continue

            s = CircuitSpeedLimit()
            s.id                 = int(new_flag) + 1
            s.circuit_id         = row["MapId"]
            s.in_use             = row["InUse"]
            s.speed              = row["Speed"]
            s.speed_unit         = row["SpeedUnit"]
            s.max_overspeed_secs = row["MaxOverspeedSecs"]
            s.detected_by_unit   = row["DetectedByUnit"]
            s.create_report      = row["Report"]

            result.append(s)

        Logger.info(f"Composed {len(result)} circuit speed limits")
        return result

    def _write_(self, new_cursor, limits: list[CircuitSpeedLimit]):

        new_cursor.execute("DELETE FROM t_circuit_speed_limits")

        sql = """
            INSERT INTO t_circuit_speed_limits (
                ID, CircuitID, InUse, Speed, SpeedUnit,
                MaxOverspeedSecs, DetectedByUnit, CreateReport
            ) VALUES (?,?,?,?,?,?,?,?)
        """

        new_cursor.executemany(sql, [s.to_db_tuple() for s in limits])
        Logger.ok(f"Written {len(limits)} records to t_circuit_speed_limits")