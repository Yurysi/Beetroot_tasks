import sqlite3


class Task2:
    def __init__(self):
        self.connection = sqlite3.connect("hr.db")
        self.cur = self.connection.cursor()

    def task2_1(self):
        self.cur.execute("SELECT first_name, last_name FROM employees")
        print(self.cur.fetchall())

    def task2_2(self):
        self.cur.execute("SELECT employee_id FROM employees")
        items = self.cur.fetchall()
        for item in items:
            print(item[0])

    def task2_3(self):
        self.cur.execute(
            "SELECT first_name, last_name, salary, salary*0.12 FROM employees ORDER BY first_name")
        elements = self.cur.fetchall()
        for element in elements:
            print(element)

    def task2_4(self):
        self.cur.execute("SELECT MAX(salary), MIN(salary)  FROM employees")
        numbers = self.cur.fetchall()
        for number in numbers:
            if number[0] > number[1]:
                print('maximal salary:', number[0])
                print('minimal salary:', number[1])

    def task2_5(self):
        self.cur.execute("SELECT first_name, last_name, ROUND(salary,2) FROM employees")
        elements = self.cur.fetchall()
        for element in elements:
            print(element)
task = Task2()
# task.task2_1()
# task.task2_2()
# task.task2_3()
# task.task2_4()
task.task2_5()
