import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="kitecmd",
        description="Kite Command Utility"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Example: hello
    hello_parser = subparsers.add_parser("hello", help="Print a greeting")
    hello_parser.add_argument("--name", "-n", default="World", help="Who to greet")

    # Example: add
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")
    add_parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    if args.command == "hello":
        print(f"Hello, {args.name}!")
    elif args.command == "add":
        print(f"Result: {args.a + args.b}")
    else:
        parser.print_help()
