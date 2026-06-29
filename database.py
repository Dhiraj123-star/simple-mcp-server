import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data.db"


def init_db():
    """Create table and insert dummy data if not exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT,
            skills TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO users (name, role, skills) VALUES (?, ?, ?)",
            [
                ("Dhiraj",  "Backend Engineer",  "Python, Django, MCP"),
                ("Alice",   "ML Engineer",       "PyTorch, LangChain, RAG"),
                ("Bob",     "DevOps Engineer",   "Docker, Kubernetes, AWS"),
                ("Sara",    "Data Scientist",    "Pandas, SQL, LlamaIndex"),
            ]
        )

    conn.commit()
    conn.close()


def get_all_users():
    """Return all users from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, role, skills FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_user_by_name(name: str):
    """Return a single user by name."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, role, skills FROM users WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    return row