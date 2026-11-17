import sqlite3

DB_NAME = "bot.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS guild_config (
                guild_id INTEGER PRIMARY KEY,
                welcome_channel_id INTEGER
            )
        """)


def set_welcome_channel(guild_id: int, channel_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO guild_config (guild_id, welcome_channel_id)
            VALUES (?, ?)
            ON CONFLICT(guild_id)
            DO UPDATE SET welcome_channel_id = excluded.welcome_channel_id
        """, (guild_id, channel_id))


def get_guild_config(guild_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("""
            SELECT welcome_channel_id
            FROM guild_config
            WHERE guild_id = ?
        """, (guild_id,))

        result = cursor.fetchone()

    if result is None:
        return {}

    return {"welcome_channel_id": result[0]}
