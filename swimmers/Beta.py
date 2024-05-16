# import the python datetime module to help us create a timestamp
from datetime import date

class Beta:
    def __init__(self, Name, Species):
        # Establish the properties of each animal
        # with a default value
        self.swimming = True
        self.name = Name
        self.species = Species
        self.date_added = date.today()