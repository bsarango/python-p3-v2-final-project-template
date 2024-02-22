#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.order import Order
import datetime
import ipdb


def reset_database():
    Employee.drop_table()
    Employee.create_table()
    Order.drop_table()
    Order.create_table()

    unit_clerk = Employee.create("Jane", "Doe", "Unit Clerk", "Neurology")
    telemetry_technician = Employee.create("Brian", "Sarango", "Telemetry Technician", "Telemetry")
    neuro_sdu_rn = Employee.create("Amy", "Jones", "Nurse", "Neurology")

    Order.create("Remote Telemetry Placement","Smith",0,telemetry_technician.id)
    Order.create("Administer Medication","Lee",1,neuro_sdu_rn.id)
    Order.create("Transfer Patient","Jones",0,unit_clerk.id)
    Order.create("Diet","Lee",0,neuro_sdu_rn.id)
    Order.create("Remote Telemetry Placement", "Jones", 0,telemetry_technician.id)

reset_database()
ipdb.set_trace()
