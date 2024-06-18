# Currency Converter CLI

A command-line interface (CLI) application that allows users to convert currency values using data from an API.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/KatanaSword/currency-converter-cli.git
   cd currency-converter-cli
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   .\.venv\Scripts\activate  # On Mac use `source .venv/bin/activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the project root directory and add your API key:
   ```
   API_KEY=your_currencyapi_key_here
   ```

## Usage

Run the Currency Converter CLI:

```sh
python app.py
```

Follow the on-screen menu to convert currency values:

1. Select to Currency Converter
2. Exit App

## Environment Variables

API_KEY: Your API key for accessing the [Currency api](https://currencyapi.com/) API.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
