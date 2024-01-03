import requests

def get_stock_info(symbol):
    api_key = 'IKF6L54JWWBJA74B'  # Replace with your Alpha Vantage API key
    base_url = 'https://www.alphavantage.co/query'

    # Make a request to the Alpha Vantage API
    response = requests.get(base_url, params={
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': api_key
    })

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract relevant information from the response
        stock_info = data['Global Quote']
        symbol = stock_info['01. symbol']
        price = stock_info['05. price']
        volume = stock_info['06. volume']
        open_price = stock_info['02. open']
        high_price = stock_info['03. high']
        low_price = stock_info['04. low']
        change_percent = stock_info['10. change percent']

        # Print the stock information
        print(f"-> Stock Symbol: {symbol}")
        print(f"-> Current Price: {price}")
        print(f"-> Volume: {volume}")
        print(f"-> Open Price: {open_price}")
        print(f"-> High Price: {high_price}")
        print(f"-> Low Price: {low_price}")
        print(f"-> Change Percent: {change_percent}")
        print("-> ")
    else:
        print(f"Error: {response.status_code} - {response.text}")


# Example usage
# stock_symbol = 'AAPL'  # Replace with the stock symbol you want to retrieve information for
# get_stock_info(stock_symbol)

def stock_info():

    command = ''
    while command != 'x':
        print('-> please type stock symbol or "x" to exit.')
        command = input("-> ")
        get_stock_info(command)

    print('-> Stock Info - Done!')

if __name__ == "__main__":
    stock_info()