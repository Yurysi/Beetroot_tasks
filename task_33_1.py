import sqlite3
import sys


class FirstTable:
    def __init__(self, db_file):
        self.db = db_file
        self.connection = None

    def create_connection(self):
        try:
            self.connection = sqlite3.connect(self.db)
            print("Sqlite version:", sqlite3.version)
        except Exception as e:
            print(e)
        return self.connection

    def create_table(self):
        # try:
        c = self.connection.cursor()
        c.execute("""CREATE TABLE articles(title text,
            full text,
            view integer,
            author text)""")

    # except Exception as e:
    #     print(e)

    def create_column(self):
        c = self.connection.cursor()
        c.execute("""INSERT INTO articles
        VALUES('Lesson 33', 'Lesson about SQLite', 7, 'Beetroot academy'),
        ('Lesson 34', 'Lesson about SQLite part2', 5, 'Beetroot academy'),
        ('Lesson 36', 'Lesson about HTTP', 1, 'Beetroot academy Taras')
        """)
        self.connection.commit()

    def update_table(self):
        c = self.connection.cursor()
        c.execute(
            "UPDATE articles SET author = 'Taras' WHERE title = 'Lesson 33'")
        self.connection.commit()

    def delete_table(self):
        c = self.connection.cursor()
        c.execute("DELETE FROM articles WHERE view <  2")
        self.connection.commit()

    def view_all(self):
        c = self.connection.cursor()
        c.execute("SELECT * FROM articles")
        elements = c.fetchall()
        for element in elements:
            sys.stdout.write(
                '| {0:10} | {1:^30} | {2:^5} | {3:10} |\n'.format(element[0],
                                                                  element[1],
                                                                  element[2],
                                                                  element[3]))

    def close_connection(self):
        self.connection.close()


f = FirstTable("task1.db")
f.create_connection()
# f.create_table()
# f.create_column()
# f.update_table()
f.delete_table()
f.view_all()
