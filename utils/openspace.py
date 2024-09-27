import random
from table import *
import pandas as pd

class Openspace():
    instances = []

    def __init__(self, tables):
        '''
        Will create an Openspace object.
        '''
        self.tables = tables
        self.number_of_tables = len(tables)
        self.instances.append(self)
        # print(self.__class__.instances)

    def __str__(self):
        return f'{self.tables},{self.number_of_tables}'

    def organize(self, names):
        '''
        Will randomly assign people to the available chairs. If there are too many people, it will inform who didn't get a chair.
        '''
        random.shuffle(names)
        index_colleague = 0

        for table in self.tables:
            while table.has_free_spot():
                print(index_colleague, len(names))

                if index_colleague < len(names):
                    table.assign_seat(names[index_colleague])

                    index_colleague += 1

                else:
                    print("Everybody seeted.")
                    break
            else:
                print("No free spot found any more")

            # print([chair.occupant for chair in table.seats])

        if len(names) > index_colleague:
            no_space = names[index_colleague:]
            print(f"Not everybody has a chair, following persons will need to stand or go home: {no_space}")



    def display(self):
        '''
        It will give an overview of all tables, give the names of the people sitting at that table and indicate if there are still free spots available at a table.
        '''
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
        '''
        This will store the seating plan in a csv file. Please not this is excluding the people that don't have a seat.
        '''
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

        df.to_csv(f'openspace-organizer/{filename}.csv')

    @classmethod
    def get_instances(self):
        return self.instances
