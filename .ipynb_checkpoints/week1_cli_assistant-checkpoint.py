# week1_cli_assistant.py
# Week 1 Project: CLI Assistant (Python fundamentals)

from datetime import datetime
import random



def show_time() -> None:
    now = datetime.now()
    print(f"\nCurrent time: {now.strftime('%I:%M %p')}\n")


def do_calculation() -> None:
    """
    Simple calculator that supports +, -, *, /
    (Kept basic on purpose for Week 1.)
    """
    print("\nCalculator (supports +, -, *, /)")
    try:
        a = float(input("Enter first number: ").strip())
        op = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: ").strip())

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("\nError: cannot divide by zero.\n")
                return
            result = a / b
        else:
            print("\nInvalid operator. Try +, -, *, or /.\n")
            return

        print(f"\nResult: {a} {op} {b} = {result}\n")
    except ValueError:
        print("\nPlease enter valid numbers.\n")


def motivation(name: str) -> None:
    print(f"\n{name}, keep going. Consistency builds engineers.\n")


def main() -> None:
    print("=== Week 1 CLI Assistant ===")
    name = input("What's your name? ").strip() or "Friend"
    quotes = [
    "Consistency beats intensity.",
    "Build daily.",
    "Debug calmly.",
    "Ship small. Improve often.",
    "Small progress compounds."
]

    while True:
        print("\nChoose an option:")
        print("1) Show current time")
        print("2) Basic calculation")
        print("3) Motivation")
        print("4) Exit")
        print("5) Random motivational quote")

        choice = input("Enter 1-5: ").strip()

        if choice == "1":
            show_time()
        elif choice == "2":
            do_calculation()
        elif choice == "3":
            motivation(name)
        elif choice == "4":
            print("\nGoodbye! See you next session.\n")
            break
        elif choice == "5":
             quote = random.choice(quotes)
             print(f"\n{quote}\n")
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.\n")


if __name__ == "__main__":
    main()