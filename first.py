class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

    def __str__(self):
        return f"{self.flight_id} {self.from_city} {self.to_city} {self.price}"

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, search_type, city1, city2=None):
        results = []
        if search_type == 1:
            for flight in self.flights:
                if flight.from_city == city1 or flight.to_city == city1:
                    results.append(flight)
        elif search_type == 2:
            for flight in self.flights:
                if flight.from_city == city1:
                    results.append(flight)
        elif search_type == 3 and city2 is not None:
            for flight in self.flights:
                if (flight.from_city == city1 and flight.to_city == city2) or (flight.from_city == city2 and flight.to_city == city1):
                    results.append(flight)
        return results

def main():
    flight_table = FlightTable()
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Welcome to the Flight Table Search Program!")
    print("Please choose a search parameter:")
    print("[1] Flights for a particular City")
    print("[2] Flights From a city")
    print("[3] Flights between two given cities")
    search_type = int(input("Enter your choice: "))
    if search_type not in [1, 2, 3]:
        print("Invalid choice. Exiting...")
        return

    city1 = input("Enter the first city: ")
    city2 = None
    if search_type == 3:
        city2 = input("Enter the second city: ")

    results = flight_table.search_flights(search_type, city1, city2)
    if len(results) > 0:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
