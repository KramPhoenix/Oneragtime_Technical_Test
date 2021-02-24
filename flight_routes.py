from itertools import combinations
from flight import Flight

class Route(object):

  #Constructor for Route
  def __init__(self, first_flight):
    self.route = [first_flight]
    self.current = 0

  def flights(self):
    return self.route

  # Functions 
  def price(self, bags):
    result = 0
    for route in self.route:
      result += route.price(bags)

    return result

  def bags_allowed(self, bags):
    for route in self.route:
      if route.bags_allowed < bags:
        return False

    return True

  def is_valid(self):
    for pair in combinations(self.route, 2):
      if (pair[0].source == pair[1].source and
        pair[0].destination == pair[1].destination):
        return False

    return True

  def source(self):
    return self.route[0].source

  def destination(self):
    return self.route[-1].destination

  def connections(self):
    connect = []
    for route in self.route[:-1]:
      connect.append(route.destination)

    connect = " -> ".join(connect)

    return connect

  def add_route(self, flight):
    self.route.append(flight)
