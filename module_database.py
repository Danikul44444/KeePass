import sqlite3
import module_hasher
from pprint import pprint
PATH = "./database/data.db"
def create_table():
    CREATE_TABLE = """CREATE TABLE IF NOT EXISTS MANAGER(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SITE TEXT,
        TITLE TEXT,
        LOGIN TEXT,
        PASSWORD TEXT
    )"""
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    cur.execute(CREATE_TABLE)
    conn.commit()
    return conn, cur

def add_info(site: str, title: str, login: str, password: str, hash: int = 256):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    cur.execute("""INSERT INTO MANAGER(SITE, TITLE, LOGIN, PASSWORD)  VALUES(?, ?, ?, ?)""", (site, title, login, module_hasher.hash(password, hash)))
    conn.commit()

def get_end_info():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM MANAGER ORDER BY id DESC LIMIT 1;""")
    return cur.fetchone()

def get_all_info():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM MANAGER ORDER BY ID""")
    data = cur.fetchall()
    return data

pprint(get_all_info())