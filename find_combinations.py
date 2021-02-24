from flight_routes import Route
from flight_functions import parse_flight_info, add_flight, display_flights_info, load_flights


def main():
  flights = []
  routes = []

  results = load_flights()

  for result in results:
    flights.append(parse_flight_info(result))

  for flight in flights:
    flight.add_connections(flights)

  for flight in flights:
    if len(flight.connections) != 0:
      routes.append(Route(flight))

  for i in range(len(routes)):
    add_flight(routes, i)
  display_flights_info(routes, 0)
  display_flights_info(routes, 1)
  display_flights_info(routes, 2)

if __name__ == "__main__":
  main()