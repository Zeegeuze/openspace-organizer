import sys
import os
import csv
import random

sys.path.append(os.path.abspath("openspace-organizer/utils"))

from table import *
from openspace import *

# set amount of tables and chairs

amount_tables = 6
amount_chairs = 4

# create chairs

chairs = []

for i in range(0, (amount_chairs * amount_tables)):
    seat = Seat()
    chairs.append(seat)

# create tables, adding correct amount of chairs per table

tables = []
start_index = 0

for i in range(0, amount_tables):
    chairs_current_table = chairs[start_index : start_index + amount_chairs]
    tables.append(Table(amount_chairs, chairs_current_table))

    start_index += amount_chairs

# create openspace

open_space = Openspace(tables)

# get colleagues in list

with open('openspace-organizer/new_colleagues.csv') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    colleagues = []
    for row in reader:
        colleagues += row

# randomly assign people to chairs

open_space.organize(colleagues)

# display the tables seats
open_space.display()

# store in excel
open_space.store("new_table_chart")
