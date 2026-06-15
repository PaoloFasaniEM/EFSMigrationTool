from structures.saved_message import SavedMessage
from services.logger import Logger

class SavedMessagesMapper:

    def _read_(self, old_cursor) -> list[SavedMessage]:
        old_cursor.execute("SELECT * FROM t_saved_messages")
        rows = old_cursor.fetchall()
        Logger.info(f"Found {len(rows)} records in t_saved_messages")
        return [self._map_row(row) for row in rows]

    def _map_row(self, row) -> SavedMessage:
        m = SavedMessage()
        m.id               = row["ID"]
        m.name             = row["Name"]
        m.width            = row["Width"]
        m.height           = row["Height"]
        m.font_size        = row["FontSize"]
        m.font_style       = row["FontStyle"]
        m.horz_alignment   = row["HorzAlignment"]
        m.vert_alignment   = row["VertAlignment"]
        m.x_margin         = row["XMargin"]
        m.y_margin         = row["YMargin"]
        m.text_color       = row["TextColor"]
        m.background_color = row["BackgroundColor"]
        m.message          = row["Message"]
        return m

    def _write_(self, new_cursor, messages: list[SavedMessage]):
        new_cursor.execute("DELETE FROM t_saved_messages")
        sql = """
            INSERT INTO t_saved_messages (
                ID, Name, Width, Height, FontSize, FontStyle,
                HorzAlignment, VertAlignment, XMargin, YMargin,
                TextColor, BackgroundColor, Message
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """
        new_cursor.executemany(sql, [m.to_db_tuple() for m in messages])
        Logger.ok(f"Written {len(messages)} records to t_saved_messages")