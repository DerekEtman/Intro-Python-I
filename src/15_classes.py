# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class Latlon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __repr__(self):
        return f'{self.lat} {self.lon}'

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(Latlon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def __repr__(self):
        return f'{self.name} {self.lon} {self.lat}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __repr__(self):
        return f'{self.name} {self.lat} {self.lon} {self.difficulty} {self.size}'


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
cata1= Waypoint("41.70505","-121.51521", "Catacombs" )

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(cata1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geo1= Geocache("44.052137", "-121.41556", "Newberry Views", "1.5", "2")
# YOUR CODE HERE


# Print it--also make this print more nicely
print(geo1)
