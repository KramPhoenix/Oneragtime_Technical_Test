from datetime import datetime, timedelta
MIN_TIME = timedelta(hours=1)
MAX_TIME = timedelta(hours=4)

class Flight(object):

  # Constructor for the Flight Class
  def __init__(self, source, destination, departure, arrival, flight_number, price, bags_allowed, bag_price):
    self.source = source
    self.destination = destination
    self.departure = departure
    self.arrival = arrival
    self.flight_number = flight_number
    self.seat_price = price
    self.bags_allowed = bags_allowed
    self.bag_price = bag_price
    self.connections = []

  # Total price foreach bag
  def price(self, bags):
    return (bags * self.bag_price) + self.seat_price

  # Add flight connection
  def add_connections(self, flights):
    for flight in flights:
      if (
          self.destination == flight.source and
          MIN_TIME <= flight.departure - self.arrival <= MAX_TIME
        ):
        self.connections.append(flight)
