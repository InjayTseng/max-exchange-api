# MAX Exchange API Automation

This project provides a convenient automation tool for creating orders on the MAX exchange platform via the official MAX exchange APIs. It's designed to streamline the order creation process, allowing for quick and efficient market operations.

## Features

- Retrieve account balances
- Calculate order prices based on target price and spread percentage
- Calculate increasing order sizes for a number of orders
- Place multiple buy and sell orders automatically
- User-friendly command-line interface
- Detailed summary and confirmation before order placement

## Prerequisites

Before you begin, ensure you have the following requirements:

- Python 3.x installed
- A MAX exchange account
- API Key and API Secret from MAX exchange

## Quick Start

1. Clone the repository or download the ZIP and extract it.
2. Navigate to the `max-exchange-api` directory.
3. Create a `.env` file in the root of the project.
4. Add your MAX exchange API Key and Secret to the `.env` file as follows:
    ```env
    MAX_API_KEY=your_api_key_here
    MAX_API_SECRET=your_api_secret_here
    ```
5. Install required dependencies (if any are listed in `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```
6. Run the script with Python:
    ```bash
    python3 main.py
    ```

## Usage Tutorial

The script will guide you through several prompts:

1. **Balance Check**: Initially, your balance will be displayed to confirm API connectivity.
2. **Order Configuration**: You will be prompted to enter the following parameters:
    - Target price
    - Spread percentage
    - Total number of orders
    - Base order size
    - Order size increment percentage
    - Trading pair (e.g., 'btcusd')
3. **Order Review**: A summary of your intended orders will be presented for review:
    - Trading Pair
    - Total Number of Orders
    - Total Buy Value
    - Total Sell Value
4. **Confirmation**: Confirm whether to proceed with order placement.

Upon confirmation, the script will automatically begin placing orders as configured.

## Contributions

Feel free to contribute to this project! If you have suggestions or improvements, please fork the repo and create a pull request or open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks!

If you'd like to support my work:

- **Ethereum Address**: `0x99141283469FF129EfC3139F963C511029aC5B66`
- **MAX Exchange Referral Code**: `https://max.maicoin.com/signup?r=a4e9431a`

## Credits

This project was made possible by the following resources:

- The initial API wrapper provided by [kulisu](https://github.com/kulisu/max-exchange-api-python3).
- Guidance and assistance from [OpenAI's ChatGPT](https://openai.com/chatgpt).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
