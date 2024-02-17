from models.__init__ import CURSOR, CONN

class Order:

    all = {}

    def __init__(self, title, ordering_doctor, completed = False, employee_id, time_stamp=None, id=None):
        self.title = title
        self.ordering_doctor = ordering_doctor
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
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self,completed):
        if isinstance(completed, bool):
            self._completed = completed
        else:
            raise ValueError("Order's completed status must be a True or False value!")

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        if isinstance(employee_id,int):
            self._employee_id = employee_id
        else:
            raise ValueError(
                "The employee entered isn't in the database. Please enter another employee to assign this order to."
            )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY
                title TEXT
                ordering_doctor TEXT
                completed BIT
                employee_id INTEGER
                time_stamp DATETIME
            )
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS orders;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO orders (title, ordering_doctor, time_stamp, completed, employee_id)
            VALUES (?,?, NOW(), ?)
        """

        CURSOR.execute(sql, (self.title, self.ordering_doctor, self.completed, self.employee_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        self.save_time_stamp(self.id)

        type(self).all[self.id] = self

    
    def save_time_stamp(self,id)
        sql = """
            SELECT * FROM orders
            WHERE id = ?
        """

        row = CURSOR.execute(sql,(id,)).fetchone()
        self.time_stamp = row[3]

    @classmethod
    def create(cls, title, ordering_doctor, time_stamp, employee_id):
        cls(title,ordering_doctor,time_stamp,employee_id)
