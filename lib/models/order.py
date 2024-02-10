from models.__init__ import CURSOR, CONN

class Order:

    all = {}

    def __init__(self, title, ordering_doctor, time_stamp, completed = False, employee_id, id=None):
        self.title = title
        self.ordering_doctor = ordering_doctor
        self.time_stamp = time_stamp
        self.completed = completed
        self.employee_id = employee_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        if isinstance(title, str) and len(title)>0:
            self._title = title
        else:
            raise ValueError("The order's title must be word(s) and cannot be empty!")

    @property
    def ordering_doctor(self):
        return self._ordering_doctor

    @ordering_doctor.setter
    def ordering_doctor(self, ordering_doctor):
        if isinstance(ordering_doctor,str) and len(ordering_doctor)>0:
            self._ordering_doctor = ordering_doctor
        else:
            raise ValueError("The ordering doctor's name has toe a be proper name and cannot be empty!")

    @property
    