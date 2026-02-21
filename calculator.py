def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(expression):
    """Parse and evaluate a simple two-operand expression like '3 + 5'."""
    ops = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    parts = expression.strip().split()
    if len(parts) != 3:
        raise ValueError("Enter an expression like: 3 + 5")

    a, op, b = parts
    if op not in ops:
        raise ValueError(f"Unknown operator '{op}'. Use +, -, *, /")

    try:
        a, b = float(a), float(b)
    except ValueError:
        raise ValueError("Operands must be numbers")

    return ops[op](a, b)


def main():
    print("Simple Calculator")
    print("Enter expressions like: 3 + 5, 10 / 2, 7 * 8")
    print("Type 'quit' to exit\n")

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            result = calculate(user_input)
            # Show as int if the result is a whole number
            if result == int(result):
                result = int(result)
            print(f"= {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
