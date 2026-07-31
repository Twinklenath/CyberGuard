import sqlite3


DATABASE = "scans.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            website TEXT,

            score INTEGER,

            scan_date DATETIME DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


def save_scan(website, score):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scans(website, score) VALUES(?, ?)",
        (website, score)
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT website,
               score,
               scan_date
        FROM scans
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    conn.close()

    return history