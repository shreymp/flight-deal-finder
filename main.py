from pprint import pprint

from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager
import datetime

manager = DataManager()
sheet_data = manager.get_data()

messager = NotificationManager()

flight_search = FlightSearch()


ORIGIN_CITY_IATA = 'ORD'

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_iata_code(row['city'])

    manager.sheet_data = sheet_data
    manager.replace_iata_codes()

from_date = datetime.date.today() + datetime.timedelta(days=1)
to_date = datetime.date.today() + datetime.timedelta(days=360)

for des in sheet_data:
    flight = flight_search.get_flight_info(ORIGIN_CITY_IATA, des['iataCode'], from_time=from_date, to_time=to_date)
    if flight != None:
        if flight.price < des['lowestPrice']:

            message = f'Low Price Alert!! Flight from {flight.departure_airport_code}, {flight.departure_city} to' \
                      f' {flight.destination_airport}, {flight.destination_city} for ${flight.price},\n' \
                      f' from {flight.out_date} to {flight.return_date}.'

            # messager.send_flight_booking_sms(message)
            pprint(message)


