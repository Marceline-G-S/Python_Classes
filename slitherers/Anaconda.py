# import the python datetime module to help us create a timestamp
from datetime import date

class Anaconda:
    def __init__(self, Name, Species):
        # Establish the properties of each animal
        # with a default value
        self.slithering = True
        self.name = Name
        self.species = Species
        self.date_added = date.today()