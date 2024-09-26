class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""

    def __str__(self):
        return f'{self.free},{self.occupant}'

    def set_occupant(self, name):
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        self.occupant = ""
        self.free = True



class Table:
    def __init__(self, capacity, seats):
        self.capacity = capacity
        self.seats = seats

    def __str__(self):
        return f'{self.capacity},{self.seats}'

    def has_free_spot(self):
        return self.left_capacity() > 0


    def assign_seat(self, name):
        [chair for chair in self.seats if chair.free][0].set_occupant(name)

    def left_capacity(self):
        return len([chair for chair in self.seats if chair.free])
