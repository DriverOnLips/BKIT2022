
class conductor:
    """дирижер"""

    def __init__(self, id, surname, salary, orch_id):
        self.id = id
        self.surname = surname
        self.salary = salary
        self.orch_id = orch_id


class orchestra:
    """оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class condOrch:
    def __init__(self, id_cond, id_orch):
        self.id_cond = id_cond
        self.id_orch = id_orch
