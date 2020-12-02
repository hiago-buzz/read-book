import sqlite3

class Connect:
    _db = 'database.db'
    _conn = ""

    def conn():
        _conn = sqlite3.connect(_db)
        return _conn

    def close():
        return _conn.close()