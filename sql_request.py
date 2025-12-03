import sqlite3

def create_db():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            test_id INT,
            question_text TEXT,
            correct_answer TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            user_id INT,
            test_id INT,
            score INT
        )
        """
    )
    con.close()

def create_survey(title,description):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(
        f"""
        INSERT INTO tests(title,description)
            VALUES ({title},{description})
        """
    )
    con.commit()
    con.close()

def delete_survey(title):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(
        f"""
            DELETE FROM tests
            WHERE title = {title}
        """
    )
    con.commit()
    con.close()

def all_surveys():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    responce = cur.execute(
        f"""
            SELECT title, description, ... FROM tests
        """
    ).fetchall()
    con.commit()
    con.close()
    return responce
