
class FlightData:
    def __init__(self, price, departure_city, departure_airport_code, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
