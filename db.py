import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('url_shortener.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS urls
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      short_url TEXT NOT NULL,
                      long_url TEXT NOT NULL)''')
        conn.commit()
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("SQLite error:", e)

create_database()
