import requests

sheety_endpoint = 'https://api.sheety.co/784f3222d3fa9d0d07e11b6ae06eddea/flightDeals/prices'
bearer_token = ''

headers = {
    'Authorization': f'Bearer {bearer_token}'
}


class DataManager:

    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(url=sheety_endpoint)
        response.raise_for_status()
        self.sheet_data = response.json()['prices']
        return self.sheet_data

    def replace_iata_codes(self):
        for city in self.sheet_data:
            iata_info = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }

            response = requests.put(url=f'{sheety_endpoint}/{city["id"]}', json=iata_info)
            print(response.text)
