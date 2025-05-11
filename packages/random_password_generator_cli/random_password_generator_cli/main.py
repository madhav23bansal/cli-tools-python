import argparse
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument(
        "--length", type=int, default=12, help="Length of the password (default: 12)"
    )
    args = parser.parse_args()

    if args.length <= 0:
        print("Error: Length must be a positive integer.")
        return

    password = generate_password(args.length)
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
