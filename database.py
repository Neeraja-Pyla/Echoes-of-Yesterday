
import sqlite3
from datetime import datetime

DATABASE_NAME = "memories.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            person TEXT,
            description TEXT NOT NULL,
            story TEXT NOT NULL,
            memory_type TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    # Safely upgrade existing databases
    cursor.execute("PRAGMA table_info(memories)")
    columns = [column[1] for column in cursor.fetchall()]

    if "image_path" not in columns:
        cursor.execute("""
            ALTER TABLE memories
            ADD COLUMN image_path TEXT
        """)

    connection.commit()
    connection.close()


def save_memory(
    title,
    person,
    description,
    story,
    memory_type,
    image_path=None
):

    connection = get_connection()
    cursor = connection.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute("""
        INSERT INTO memories (
            title,
            person,
            description,
            story,
            memory_type,
            created_at,
            image_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        person,
        description,
        story,
        memory_type,
        created_at,
        image_path
    ))

    connection.commit()
    connection.close()


def get_all_memories():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            person,
            description,
            story,
            memory_type,
            created_at,
            image_path
        FROM memories
        ORDER BY id DESC
    """)

    memories = cursor.fetchall()
    connection.close()

    return memories


def delete_memory(memory_id):

    connection = get_connection()
    cursor = connection.cursor()

    # Retrieve photograph path before deleting
    cursor.execute(
        "SELECT image_path FROM memories WHERE id = ?",
        (memory_id,)
    )

    result = cursor.fetchone()

    cursor.execute(
        "DELETE FROM memories WHERE id = ?",
        (memory_id,)
    )

    connection.commit()
    connection.close()

    return result[0] if result else None
