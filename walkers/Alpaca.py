# import the python datetime module to help us create a timestamp
from datetime import date

class Alpaca:
    def __init__(self, Name, Species, Shift, food):
        # Establish the properties of each animal
        # with a default value
        self.walking = True
        self.name = Name
        self.species = Species
        self.shift = Shift
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"