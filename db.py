import sqlite3

DB_NAME = "course.db"

connection = sqlite3.connect(DB_NAME, check_same_thread=False)


def create_course(name: str, course_credits: int, term: str, tutor: int):
    """
    Create a new course in the database with the given parameters

    Returns an auto incremented id
    """
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO course (name, credits, term, tutor) VALUES (?, ?, ?, ?)",
        (name, course_credits, term, tutor),
    )

    course_id = cursor.lastrowid
    cursor.commit()

    return course_id


