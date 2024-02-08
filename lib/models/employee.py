from models.__init__ import CURSOR, CONN

class Employee():

    all = {}

    def __init__(self,first_name, last_name, job_title, department, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.department = department



