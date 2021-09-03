import sqlite3


def connect_db():
    db = sqlite3.connect('database.db')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments '
                        '(id INTEGER PRIMARY KEY, '
                        'comment TEXT)')
    db.commit()
    return db


def add_comment(comment):
    db = connect_db()
    db.cursor().execute('INSERT INTO comments (comment) '
                        'VALUES (?)', (comment,))
    db.commit()

def fetch_comment():
          db = connect_db()
          cur = db.cursor()  
          comments = []
          cur.execute("SELECT comment from comments")
          rows = cur.fetchall()
          for row in rows:
                    comments.append(row)
          return comments
