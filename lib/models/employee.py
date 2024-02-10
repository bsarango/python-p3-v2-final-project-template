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
            raise ValueError("First name must be word and cannot be blank!")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self):
        if isinstance(last_name,str) and len(last_name)>0:
            self._last_name
        else:
            raise ValueError("Last name must be a word and cannot be blank!")

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self,job_title):
        if isinstance(job_title,str) and len(job_title)>0:
            self._job_title = job_title
        else:
            raise ValueError("The job title must be word(s) and cannot be blank!")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self,department):
        if isinstance(department,str) and len(department):
            self._department = department
        else:
            raise ValueError("The department has to be a word(s) and cannot be blank!")


