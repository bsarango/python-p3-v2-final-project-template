from models.__init__ import CURSOR, CONN
import datetime
import cli_color_py

class Order:

    all = {}

    def __init__(self, title, ordering_doctor, completed, employee_id, time_stamp=None, id=None):
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
            raise ValueError(cli_color_py.red("The order's title must be word(s) and cannot be empty!"))

    @property
    def ordering_doctor(self):
        return self._ordering_doctor

    @ordering_doctor.setter
    def ordering_doctor(self, ordering_doctor):
        if isinstance(ordering_doctor,str) and len(ordering_doctor)>0:
            self._ordering_doctor = ordering_doctor
        else:
            raise ValueError(cli_color_py.red("The ordering doctor's name has toe a be proper name and cannot be empty!"))

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self,completed):
        if isinstance(completed, int) and (completed == 1 or completed ==0):
            self._completed = completed
        else:
            raise ValueError(cli_color_py.red("Order's completed status must be either 0 or 1!"))

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        if isinstance(employee_id,int):
            self._employee_id = employee_id
        else:
            raise ValueError(cli_color_py.red(
                "The employee entered isn't in the database. Please enter another employee to assign this order to."
            ))

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            title TEXT,
            ordering_doctor TEXT,
            completed BIT,
            employee_id INTEGER,
            time_stamp TEXT)
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

        self.time_stamp = str(datetime.datetime.now())

        sql = """
            INSERT INTO orders (title, ordering_doctor, completed, employee_id, time_stamp)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.ordering_doctor, self.completed, self.employee_id, self.time_stamp))
        CONN.commit()

        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self


    @classmethod
    def create(cls, title, ordering_doctor, completed, employee_id):
        order = cls(title,ordering_doctor, completed ,employee_id)
        order.save()
        return order

    def update(self):
        sql = """
            UPDATE orders
            SET title = ?, ordering_doctor=?, completed=?, employee_id=?
            WHERE id = ?
        """

        CURSOR.execute(sql,(self.title, self.ordering_doctor,self.completed, self.employee_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM orders
            WHERE id = ?
        """

        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        order = cls.all.get(row[0])

        if order:
            order.title = row[1]
            order.ordering_doctor = row[2]
            order.completed = row[3]
            order.employee_id = row[4]
            order.save_time_stamp = row[5]

        else:
            order = cls(row[1], row[2], row[3], row[4])
            order.id = row[0]
            cls.all[order.id] = order
            order.time_stamp = row[5]

        return order

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM orders
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT * FROM orders
            WHERE id = ?
        """

        row = CURSOR.execute(sql,(id,)).fetchone()

        return cls.instance_from_db(row) if row else None

    def employee(self):
        from models.employee import Employee
        employee = Employee.find_by_id(self.employee_id)
        return employee