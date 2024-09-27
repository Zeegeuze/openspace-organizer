class Seat:
    def __init__(self):
        '''
        Initiates a seat Object.
        '''
        self.free = True
        self.occupant = ""

    def __str__(self):
        return f'{self.free},{self.occupant}'

    def set_occupant(self, name):
        '''
        Will add an occupant to a chair and set free to False.
        '''
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        '''
        Removes an occupant from a chair by adding an empty string. The free will be moved to True.
        '''
        self.occupant = ""
        self.free = True



class Table:
    def __init__(self, capacity, seats):
        """
        Creates a table object.
        """
        self.capacity = capacity
        self.seats = seats

    def __str__(self):
        return f'{self.capacity},{self.seats}'

    def has_free_spot(self):
        '''
        Returns a boolean indicating if a table has free chairs.
        '''
        return self.left_capacity() > 0


    def assign_seat(self, name):
        '''
        will assign a name of a person to a free chair. Will not set a name if no chairs are available.
        '''
        [chair for chair in self.seats if chair.free][0].set_occupant(name)

    def left_capacity(self):
        '''
        Returns the amount of free chairs available on the table.
        '''
        return len([chair for chair in self.seats if chair.free])
