from models.__init__ import CURSOR, CONN

class Order:
    def __init__(self, title, ordering_doctor, time_stamp, completed, employee_id, id=None):
        self.title = title
        self.ordering_doctor = ordering_doctor
        self.time_stamp = time_stamp
        self.completed = completed
        self.employee_id = employee_id
