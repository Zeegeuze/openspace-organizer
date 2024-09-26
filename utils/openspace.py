import random
from table import *
import pandas as pd

class Openspace:
    def __init__(self, tables):
        self.tables = tables
        self.number_of_tables = len(tables)

    def __str__(self):
        return f'{self.tables},{self.number_of_tables}'

    def organize(self, names):
        random.shuffle(names)
        index_colleague = 0

        for table in self.tables:
            while table.has_free_spot():
                table.assign_seat(names[index_colleague])

                index_colleague += 1

            else:
                print("No free spot found any more")

            # print([chair.occupant for chair in table.seats])

        if len(names) > index_colleague:
            no_space = names[index_colleague:]
            print(f"Not everybody has a chair, following persons will need to stand or go home: {no_space}")



    def display(self):
        count = 1
        for table in self.tables:
            people_at_table = [chair.occupant for chair in table.seats]

            print(f"Following colleagues are sitting at table {count}:")
            for colleague in people_at_table:
                print(colleague)

            if len(people_at_table) != table.capacity:
                available_spots = table.capacity - len(people_at_table)
                print(f"There are still {available_spots} available spots at this table.")

            count += 1


    def store(self, filename):
        column_names = []
        names = []
        count = 1

        for table in self.tables:
            column_names.append(f"Table {count}")
            count += 1
            names.append([chair.occupant for chair in table.seats])

        df = pd.DataFrame(
            names,
            index=column_names
        )

        df.to_csv(f'{filename}.csv')
