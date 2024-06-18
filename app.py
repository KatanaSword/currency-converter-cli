import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

class Currency_Converter:
    def __init__(self, from_country, to_country, from_currency):
        self.from_country = from_country
        self.to_country = to_country
        self.from_currency = from_currency
        self.url = "https://api.currencyapi.com/v3/latest"
        self.headers = {
            'apikey': config["API_KEY"]
        }
        self.response = None
        self.values = None

    def get_value(self):
        self.values = self.response["data"]

    def get_from_country(self):
        self.values[self.from_country]["value"]

    def get_to_country(self):
        self.value[self.to_country]["value"]

    def get_convert(self):
        try:
            response = requests.request("GET", self.url, headers=self.headers)
            self.response = response.json()
        except ValueError as vr:
            print(vr)
        except Exception as e:
            print(f"{e}")

def main():
    while True:
        print(f"\n{"*"*30} Currency Converter {"*"*30}")
        print("1. Select to Currency Converter.")
        print("0. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"\n{"*"*30} Select Country {"*"*30}")
            from_country = input("From country: ")
            from_currency = input("From number of currency: ")
            to_country = input("To country: ")
            convert = Currency_Converter(from_country, from_currency, to_country)
            convert.get_convert()
        elif choice == "0":
            break
        else:
            print("Invalid choice, Try again")

if __name__ == "__main__":
    main()
