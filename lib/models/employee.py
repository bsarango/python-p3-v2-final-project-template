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

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                job_title TEXT,
                department TEXT)
            """
            CURSOR.execute(sql)
            CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employees;
            """
            CURSOR.execute(sql)
            CONN.commit()

    def save(self):
        sql = """
            INSERT INTO employees (first_name, last_name, job_title, department)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql,(self.first_name, self.last_name, self.job_title, self.department))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name, job_title, department):
        employee =  cls(first_name, last_name, job_title, department)
        employee.save()
        return employee

    def update(self):
        sql = """
            UPDATE employees
            SET first_name = ?, last_name = ?, job_title = ?, department = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.job_title, self.department, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        employee = cls.all.get(row[0])

        if employee :
            employee.first_name=row[1]
            employee.last_name=row[2]
            employee.job_title=row[3]
            employee.department=row[4]
        
        else:
            employee = cls(row[1],row[2],row[3],row[4])
            employee.id = row[0]
            cls.all[employee.id] = employee

        return employee


    def get_all(self):
        sql = """
            SELECT * from employees
        """

        rows = CURSOR.execute(sql).fetchall()
        
        return [row from row in rows]