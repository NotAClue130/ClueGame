import pymysql
import cryptography


def create_table_users(db):
    cursor = db.cursor()
    sql = """
    CREATE TABLE Users
(
    username text,
    sid integer,
    PRIMARY KEY (username)
)
    """
    cursor.execute(sql)
    db.commit()
    db.close()
    return 0


def create_table_characters(db):
    cursor = db.cursor()
    sql = """
    CREATE TABLE Characters
(
    character text,
    username text,
    action text,
    status text,
    card text,
    PRIMARY KEY (character)
)
        """
    cursor.execute(sql)
    db.commit()
    db.close()
    return 0


def insert_table_users(db, username, sid):
    cursor = db.cursor()
    sql = """
    INSERT INTO Users (
	username, sid)
	VALUES (%s, %s);
    """
    cursor.execute(sql, (username, sid))
    db.commit()
    db.close()
    return 0


def query_table_characters(db):
    cursor = db.cursor()
    sql = """
    SELECT
    character, username, action, status, card
    FROM
    Characters
    """
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def query_table_users_on_sid(db, sid):
    cursor = db.cursor()
    sql = """
    SELECT username
	FROM Users
	WHERE sid=%s
    """
    cursor.execute(sql)
    res = cursor.fetchall()[0][0]
    return res


def insert_table_characters(db, character, username):
    cursor = db.cursor()
    sql = """
    INSERT INTO Characters(
	character, username)
	VALUES (%s, %s);
        """
    cursor.execute(sql, (character, username))
    db.commit()
    db.close()
    return 0


def query_table_characters_on_username(db, username):
    cursor = db.cursor()
    sql = """
    SELECT character
	FROM Characters
	WHERE username=%s
            """
    cursor.execute(sql, (username,))
    res = cursor.fetchall()[0][0]
    return res


def delete_table_characters_on_username(db, username):
    cursor = db.cursor()
    sql = """
        DELETE FROM Characters
        WHERE username=%s
            """
    cursor.execute(sql, (username,))
    db.commit()
    db.close()
    return 0
