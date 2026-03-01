# week1_cli_assistant.py
# Week 1 Project: CLI Assistant (Python fundamentals)

from datetime import datetime


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

    while True:
        print("\nChoose an option:")
        print("1) Show current time")
        print("2) Basic calculation")
        print("3) Motivation")
        print("4) Exit")

        choice = input("Enter 1-4: ").strip()

        if choice == "1":
            show_time()
        elif choice == "2":
            do_calculation()
        elif choice == "3":
            motivation(name)
        elif choice == "4":
            print("\nGoodbye! See you next session.\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()