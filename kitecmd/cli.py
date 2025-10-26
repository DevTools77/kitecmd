import argparse
import requests
import sys
from importlib.metadata import version, PackageNotFoundError


def main():
    parser = argparse.ArgumentParser(
        prog="kitecmd",
        description="Kite Command Utility"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # === hello command ===
    hello_parser = subparsers.add_parser("hello", help="Print a greeting")
    hello_parser.add_argument("--name", "-n", default="World", help="Who to greet")

    # === add command ===
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")
    add_parser.add_argument("b", type=float, help="Second number")

    # === checkupdate command ===
    subparsers.add_parser("checkupdate", help="Check if a new version is available on PyPI")

    args = parser.parse_args()

    # --- Command logic ---
    if args.command == "hello":
        print(f"Hello, {args.name}!")

    elif args.command == "add":
        print(f"Result: {args.a + args.b}")

    elif args.command == "checkupdate":
        check_for_update("kitecmd")

    else:
        parser.print_help()


def check_for_update(package_name):
    """Check PyPI for the latest version of this package."""
    try:
        current_version = version(package_name)
    except PackageNotFoundError:
        print("⚠️  Unable to detect installed version.")
        sys.exit(1)

    try:
        resp = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=5)
        resp.raise_for_status()
        latest_version = resp.json()["info"]["version"]
    except requests.RequestException as e:
        print(f"❌ Could not fetch update info: {e}")
        sys.exit(1)

    if current_version == latest_version:
        print(f"✅ You are using the latest version ({current_version})")
    else:
        print(f"⬆️  A new version is available!")
        print(f"   Installed: {current_version}")
        print(f"   Latest:    {latest_version}")
        print(f"👉 To update, run: pip install --upgrade {package_name}")
