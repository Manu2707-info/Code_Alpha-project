from dataclasses import dataclass
from typing import List


@dataclass
class StockPosition:
    symbol: str
    quantity: int
    price: float
    investment: float


STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 150.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
}


def display_stock_list() -> None:
    print("=" * 60)
    print("                STOCK TRACKER")
    print("=" * 60)
    print("\nAvailable Stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<6} : ${price:,.2f}")


def get_valid_integer(prompt: str, minimum: int = 1) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Please enter a value greater than or equal to {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def add_positions() -> List[StockPosition]:
    portfolio: List[StockPosition] = []
    number_of_stocks = get_valid_integer("\nHow many stocks do you want to add? ", minimum=1)

    for index in range(number_of_stocks):
        print(f"\nStock {index + 1}")

        while True:
            symbol = input("Enter stock symbol: ").strip().upper()
            if symbol in STOCK_PRICES:
                break
            print("Invalid stock symbol! Please choose from the available list.")

        quantity = get_valid_integer("Enter quantity: ", minimum=1)
        price = STOCK_PRICES[symbol]
        investment = price * quantity

        portfolio.append(
            StockPosition(
                symbol=symbol,
                quantity=quantity,
                price=price,
                investment=investment,
            )
        )
        print(f"Added {quantity} shares of {symbol} successfully.")

    return portfolio


def display_portfolio(portfolio: List[StockPosition]) -> float:
    total_investment = sum(position.investment for position in portfolio)

    print("\n" + "=" * 80)
    print("".join([" " * 18, "YOUR PORTFOLIO"]))
    print("=" * 80)

    if not portfolio:
        print("No stocks were added.")
        return total_investment

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<15}{'Investment':<18}")
    print("-" * 80)

    for position in portfolio:
        print(
            f"{position.symbol:<10}"
            f"{position.quantity:<12}"
            f"${position.price:<13,.2f}"
            f"${position.investment:<16,.2f}"
        )

    print("-" * 80)
    print(f"Total Investment: ${total_investment:,.2f}")
    return total_investment


def save_portfolio(portfolio: List[StockPosition], total_investment: float, filename: str = "stock_tracker.txt") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write("STOCK TRACKER\n")
        file.write("=" * 50 + "\n")

        for position in portfolio:
            file.write(
                f"Stock: {position.symbol}, "
                f"Quantity: {position.quantity}, "
                f"Price: ${position.price:,.2f}, "
                f"Investment: ${position.investment:,.2f}\n"
            )

        file.write("=" * 50 + "\n")
        file.write(f"Total Investment: ${total_investment:,.2f}\n")

    print(f"Result successfully saved to {filename}")


def main() -> None:
    display_stock_list()

    portfolio = add_positions()
    total_investment = display_portfolio(portfolio)

    save_choice = input("\nDo you want to save the result? (yes/no): ").strip().lower()
    if save_choice == "yes":
        save_portfolio(portfolio, total_investment)
    else:
        print("Result was not saved.")

    print("\nThank you for using Stock Tracker!")


if __name__ == "__main__":
    main()