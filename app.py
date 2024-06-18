import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

class Currency_Converter:
    def __init__(self, from_country = None, to_country = None, from_currency = None):
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

    def get_currency_code(self):
        if not self.from_country or not self.to_country:
            print("\nPlease enter country code, Try again")
            return

        countryOne = self.values[self.from_country]["code"]
        countryTwo = self.values[self.to_country]["code"]
        print(f"\n{"*"*30} From {countryOne} To {countryTwo} {"*"*30}")

    def get_country(self):
        if not self.from_country or not self.to_country:
            print("\nPlease enter country code, Try again")
            return

        currencyOne = self.values[self.from_country]["value"]
        currencyTwo = self.values[self.to_country]["value"]

        convert = (float(currencyTwo) * float(self.from_currency)) / float(currencyOne)
        print(f"Currency Convert: {convert:.2f} {self.values[self.to_country]["code"]}")

    def get_convert(self):
        try:
            response = requests.request("GET", self.url, headers=self.headers)
            self.response = response.json()
            if response.status_code != 200:
                print("\nFailed to retrieve data from the API")
                return

            self.get_value()
            self.get_currency_code()
            self.get_country()
        except ValueError as vr:
            print(vr)
        except Exception as e:
            print(e)

def main():
    while True:
        print(f"\n{"*"*30} Currency Converter {"*"*30}")
        print("1. Select to Currency Converter.")
        print("0. Exit App")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print(f"\n{"*"*30} Select Country {"*"*30}")
            from_country = input("From country: ")
            from_currency = input("currency: ")
            to_country = input("To country: ")
            convert = Currency_Converter(from_country = from_country.strip().upper(), from_currency = from_currency, to_country = to_country.strip().upper())
            convert.get_convert()
        elif choice == "0":
            break
        else:
            print("Invalid choice, Try again")

if __name__ == "__main__":
    main()
