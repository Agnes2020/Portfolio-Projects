# Author: Agnes Fusese
from Property_class import Property


# importing the parent file.
class House(Property):
    def __init__(self, location, rent_out_times, price, rented, numberofrooms):
        super().__init__(location, rent_out_times, price, rented)
        self.numberOfRooms = numberofrooms

    def house_info(self):
        # this method will display information of the land to the ordinary user based on input
        return "Location of House: " + self.PropertyLocation + "\n Price of the House: " + \
               str(self.price) + "\n Number of rooms available: " + str(self.numberOfRooms)

    def house_rented(self):
        # This method is used to mark the property as rented once a user rents it
        self.rented = True

    def status(self):
        # This method Checks whether the property is rented and returns the status of the property
        if self.rented:
            return "Rented"
        else:
            return "Not Rented"

    def __str__(self):
        return self.status()
