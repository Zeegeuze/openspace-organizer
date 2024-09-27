import sys
import os
import csv

sys.path.append(os.path.abspath("openspace-organizer/utils"))

from table import *
from openspace import *

# Ask if we're adding an extra person or creating a new floor plan
floorplan_input = input("Type 'new' if you want to create a new floorplan or 'add' if you want to add a person to the existing floorplan.")

# checking for wrong entry
while (floorplan_input != 'new' and floorplan_input != 'add'):
    floorplan_input = input("Wrong entry. Type 'new' if you want to create a new floorplan or 'add' if you want to add a person to the existing floorplan.")


if floorplan_input == 'new':
    new_floorplan = True
elif floorplan_input == 'add':
    new_floorplan = False

if new_floorplan == True:
    # set amount of tables and chairs

    amount_tables = int(input("How many table are in the office? Please add a number"))
    amount_chairs = int(input("How many chairs do you have per table? Please add a number"))

    print(f"The maximum capacity is {amount_chairs * amount_tables} spaces")

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

    # Ask if they want to add a list or a csv
    list_or_csv = input("Type 'csv' if you want to use the csv. Otherwise type or copy the persons you want to add, separated by commas")

    if list_or_csv != 'csv':
        # change input into a list

        colleagues = list(list_or_csv.split(', '))
    else:
        # download csv and get colleagues in list

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

else:
    print("Sorry, we don't support that yet")
#     # get extra persons

#     extra_persons_input = input("Please put the extra persons you want to seat, separated by a comma")
#     extra_persons = list(extra_persons_input.split(', '))

#     open_space.organize(extra_persons)
