from Class import Vehicle

class Car(Vehicle):

    def __init__(self, identifier, assigned_lot=None):
        super.__init__(identifier, 'Car', assigned_lot)

