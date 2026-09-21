import sqlite3


DATABASE_NAME = "study_planner.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            task TEXT NOT NULL,
            date TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_task_db(subject, task, date, priority):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO tasks
            (subject, task, date, priority, status)
            VALUES (?, ?, ?, ?, ?)
        """, (subject, task, date, priority, "pending"))

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        print("Database error:", error)


def get_tasks():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
        """)

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def complete_task_db(task_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE tasks
            SET status = 'completed'
            WHERE id = ?
        """, (task_id,))

        if cursor.rowcount == 0:
            print("Task ID does not exist.")
        else:
            connection.commit()

        connection.close()

    except sqlite3.Error as error:
        print("Database error:", error)


def delete_task_db(task_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?
        """, (task_id,))

        if cursor.rowcount == 0:
            print("Task ID does not exist.")
        else:
            connection.commit()

        connection.close()

    except sqlite3.Error as error:
        print("Database error:", error)


def count_tasks_db():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM tasks")

        count = cursor.fetchone()[0]

        connection.close()

        return count

    except sqlite3.Error as error:
        print("Database error:", error)
        return 0


def search_task_db(keyword):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE subject LIKE ?
               OR task LIKE ?
               OR date LIKE ?
               OR priority LIKE ?
               OR status LIKE ?
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def filter_subject_db(subject):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE subject LIKE ?
        """, (f"%{subject}%",))

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def pending_tasks_db():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE status = 'pending'
        """)

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def completed_tasks_db():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE status = 'completed'
        """)

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def medium_priority_db():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE priority = 'Medium'
        """)

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def low_priority_db():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE priority = 'Low'
        """)

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def deadline_tasks_db(date):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE date = ?
        """, (date,))

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []


def upcoming_tasks_db():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, subject, task, date, priority, status
            FROM tasks
            WHERE status = 'pending'
        """)

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    except sqlite3.Error as error:
        print("Database error:", error)
        return []