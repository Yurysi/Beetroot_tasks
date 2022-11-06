class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def __name__(self):
        return self.name

    def __repr__(self):
        return f'{self.name}'


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            print(f'{new_boss.name} is not a boss!')

    def __name__(self):
        return self.name

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.company}, {self.boss}'


boss_1 = Boss(321, 'Denis', 'Nova Poshta')
boss_2 = Boss(711, 'Stepan', 'Glovo')
worker_1 = Worker(123, 'Pete', 'Nova Poshta', boss_1)
worker_2 = Worker (117, 'Oleg', 'Glovo', boss_2)









