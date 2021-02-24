import sys
import locale
from datetime import datetime
from flight import Flight
from flight_routes import Route
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

def load_flights():
  flights = sys.stdin.read().splitlines()
  return flights[1:]


def parse_flight_info(flight):
  results = flight.split(",")

  results[2] = datetime.strptime(results[2], DATE_FORMAT)
  results[3] = datetime.strptime(results[3], DATE_FORMAT)
  results[5] = int(results[5])
  results[6] = int(results[6])
  results[7] = int(results[7])

  return Flight(*results)

def add_flight(routes, index):
  route = routes[index]

  if len(route.flights()[-1].connections) == 0:
    return routes

  if len(route.flights()[-1].connections) > 1:
    for connection in route.flights()[-1].connections[1:]:
      new = Route(route.flights()[0])

      for flight in route.flights()[1:]:
        new.add_route(flight)

      new.add_route(connection)
      routes.append(new)

  route.add_route(route.flights()[-1].connections[0])

  add_flight(routes, index)

  return routes

def display_flights_info(routes, bags):
  locale.setlocale(locale.LC_ALL, '')
  sys.stdout.write("\n")
  text = "Flights that allow {} bag(s)" . format(bags)
  sys.stdout.write(text)
  sys.stdout.write("\n")

  for route in routes:
    if route.is_valid() and route.bags_allowed(bags):
      itinerary = "{} -> {} -> {}, Total price: {} \n" .format(route.source(), route.connections(
      ), route.destination(), locale.currency(route.price(bags), grouping=True))

      sys.stdout.write(itinerary)

  sys.stdout.write("\n")
