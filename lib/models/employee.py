from models.__init__ import CURSOR, CONN

class Employee:

    all = {}

    def __init__(self, first_name, last_name, job_title, department, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.department = department


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,first_name):
        if isinstance(first_name,str) and len(first_name)>0:
            self._first_name = first_name
        else:
            raise ValueError("Last name must be a non-empty string")

    

