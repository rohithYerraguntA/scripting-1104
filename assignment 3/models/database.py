import sqlite3

DB_NAME = 'logs.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            event_time TEXT,
            event_name TEXT,
            username TEXT,
            source_ip TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_log(logs):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for log in logs:
        cursor.execute('''
            INSERT INTO logs (event_time, event_name, username, source_ip)
            VALUES (?, ?, ?, ?)
        ''', (log['event_time'], log['event_name'], log['username'], log['source_ip']))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs')
    logs = cursor.fetchall()
    conn.close()
    return logs
