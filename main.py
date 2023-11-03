from max.client import Client
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
api_key = os.getenv('MAX_API_KEY')
api_secret = os.getenv('MAX_API_SECRET')

def calculate_order_prices(target_price, spread_percentage, total_orders):
    """
    Calculate the buy and sell order prices based on the target price, spread percentage, and total number of orders.

    :param target_price: The target midpoint price for the market maker.
    :param spread_percentage: The desired spread percentage.
    :param total_orders: The total number of buy and sell orders to place.
    :return: Two lists containing the buy prices and sell prices.
    """
    buy_prices = []
    sell_prices = []

    for i in range(total_orders):
        spread_multiplier = (1 - spread_percentage / 100) ** (i + 1)
        buy_prices.append(target_price * spread_multiplier)
        sell_prices.append(target_price / spread_multiplier)

    return buy_prices, sell_prices

def calculate_increasing_order_sizes(base_size, increment, total_orders):
    """
    Calculate order sizes, increasing with each subsequent order.

    :param base_size: The size for the first order.
    :param increment: The increment factor by which each subsequent order is increased.
    :param total_orders: The total number of orders.
    :return: A list containing the sizes for each order.
    """
    return [base_size * (1 + increment) ** i for i in range(total_orders)]

def calculate_total_order_value(prices, sizes):
    """
    Calculate the total value of orders based on prices and sizes.

    :param prices: A list of prices for the orders.
    :param sizes: A list of sizes for the orders.
    :return: The total value of all the orders.
    """
    return sum(price * size for price, size in zip(prices, sizes))

def cancel_all_orders(client, pair, side):
    """
    Cancel all orders for a given trading pair and side.

    :param client: The API client instance.
    :param pair: The trading pair (e.g., 'maxtwd').
    :param side: The side of the orders to cancel ('sell' or 'buy').
    :return: The result of the API call.
    """
    result = client.set_private_cancel_orders(pair, side)
    return result

def get_order_history(client, pair, states):
    """
    Get the order history for a given trading pair and states.

    :param client: The API client instance.
    :param pair: The trading pair to query.
    :param states: A list of states to filter the orders by.
    :return: The result of the API call.
    """
    result = client.get_private_order_history(pair, states)
    return result

def place_single_order(client, pair, side, volume, price):
    """
    Place a single order.

    :param client: The API client instance.
    :param pair: The trading pair for the order (e.g., 'btcusd').
    :param side: The side of the order ('buy' or 'sell').
    :param volume: The volume of the order.
    :param price: The price at which to place the order.
    :return: The result of the API call.
    """
    result = client.set_private_create_order(pair, side, volume, price)
    return result

def create_orders(client, pair, sides, sizes, prices, types):
    """
    Create orders using the provided client instance.

    :param client: The API client instance.
    :param pair: The trading pair.
    :param sides: A list of order sides ('buy' or 'sell').
    :param sizes: A list of order sizes.
    :param prices: A list of order prices.
    :param types: A list of order types (e.g., 'limit', 'market').
    :return: The API result for the order creation.
    """
    result = client.set_private_create_orders(pair, sides, sizes, prices, _types=types)
    return result

def get_and_display_account_balances(client):

    """
    Fetches the account balances from the client and displays them in a formatted way.

    :param client: The API client instance.
    """
    results = client.get_private_account_balances()

    # Initialize a list to hold formatted balance information
    formatted_balances = []

    # Process each result in the list
    for balance in results:
        currency = balance['currency']
        amount = float(balance['balance'])
        if amount > 0:  # Filter out zero balances
            formatted_balances.append((currency, amount))

    # Sort the balances by amount in descending order
    sorted_balances = sorted(formatted_balances, key=lambda x: x[1], reverse=True)

    # Print the formatted balances
    if sorted_balances:
        print("[I] Your Account Balances:")
        for currency, amount in sorted_balances:
            print(f"    {currency}: {amount:.4f}")
    else:
        print("[I] No non-zero balances found.")

    print()  # Print a newline for better separation

def main():
    
    client = Client(api_key, api_secret)
    
    # Make the API call to get account balances
    # Display account balances
    get_and_display_account_balances(client)   

    # Ask user if they want to cancel all orders or place new orders
    action = input("Do you want to cancel all orders or place new orders? Enter 'cancel' or 'place': ").strip().lower()

    # Cancel orders if chosen
    if action == 'cancel':
        trading_pair = input("Enter the trading pair to cancel orders (e.g., 'maxtwd'): ")
        side = input("Which side to cancel? Enter 'sell' or 'buy': ").strip().lower()
        cancel_result = cancel_all_orders(client, trading_pair, side)
        print(f"[I] Canceled orders for {trading_pair} on the {side} side: \n    {cancel_result}\n")
        return

    # If not canceling, proceed with placing orders
    # User input for target price, spread percentage, total number of orders, and base order size
    
    target_price = float(input("Enter the target price: ")) 

    spread_percentage = float(input("Enter the spread percentage: (0.5-5) "))

    total_orders = int(input("Enter the total number of orders: (20-50) "))

    base_order_size = float(input("Enter the base order size: "))

    # 5%-10%
    order_size_increment = float(input("Enter the order size increment percentage: ")) / 100

    # Calculate order prices and sizes
    buy_prices, sell_prices = calculate_order_prices(target_price, spread_percentage, total_orders)
    buy_sizes = calculate_increasing_order_sizes(base_order_size, order_size_increment, total_orders)
    sell_sizes = calculate_increasing_order_sizes(base_order_size, order_size_increment, total_orders)

    # After calculating your prices and sizes
    buy_prices = [round(price, 4) for price in buy_prices]  # Round to 4 decimal places
    sell_prices = [round(price, 4) for price in sell_prices]
    buy_sizes = [round(size, 4) for size in buy_sizes]
    sell_sizes = [round(size, 4) for size in sell_sizes]

    # Calculate and display the total value of buy and sell orders
    total_buy_value = calculate_total_order_value(buy_prices, buy_sizes)
    total_sell_value = calculate_total_order_value(sell_prices, sell_sizes)

    # User input for trading pair
    trading_pair = input("Enter the trading pair (e.g., 'btcusd'): ")

    # Display the calculated buy and sell prices and sizes
    for i, (buy_price, sell_price, buy_size, sell_size) in enumerate(zip(buy_prices, sell_prices, buy_sizes, sell_sizes), start=1):
        print(f"Buy Order {i} - Price: {buy_price:.4f}, Size: {buy_size:.2f}")
        print(f"Sell Order {i} - Price: {sell_price:.4f}, Size: {sell_size:.2f}")

    # Confirmation before placing orders
    print("\nPlease review your orders:")
    print(f"Trading Pair: {trading_pair}")
    print(f"Total Number of Orders: {total_orders}")
    print(f"Total Buy Value: {total_buy_value:.2f}")
    print(f"Total Sell Value: {total_sell_value:.2f}")

    confirm = input("\nDo you want to proceed with placing these orders? (yes/no): ").lower()
    if confirm == 'yes':
        # Place the orders if confirmed
        # ... [code to place orders] ...
        print("Orders have been placed.")
    else:
        print("Order placement canceled.")


    # Deprecated
    # # Create orders
    # # Specify the order types for buy and sell orders
    # order_types = ['limit'] * total_orders  # Assuming all orders are limit orders
    # # Create buy orders
    # create_orders(client, trading_pair, buy_prices, buy_sizes, 'buy', order_types)
    # # Create sell orders
    # create_orders(client, trading_pair, sell_prices, sell_sizes, 'sell', order_types)

    # SINGLE: Place buy and sell orders one by one 
    for buy_price, buy_size in zip(buy_prices, buy_sizes):
        buy_order_result = place_single_order(client, trading_pair, 'buy', buy_size, buy_price)
        print(f"Placed buy order at {buy_price} for size {buy_size}: {buy_order_result}")

    for sell_price, sell_size in zip(sell_prices, sell_sizes):
        sell_order_result = place_single_order(client,trading_pair, 'sell', sell_size, sell_price)
        print(f"Placed sell order at {sell_price} for size {sell_size}: {sell_order_result}")

if __name__ == "__main__":
    main()