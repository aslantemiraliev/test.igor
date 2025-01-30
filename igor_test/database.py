import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path


    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS complaint(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                inst TEXT,
                text TEXT,
            )
            """)



    def save_compl(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO complaint (name, inst, text)
                VALUES (?, ?, ?)
            """,
                (data["name"], data["inst"], data["text"])
            )
