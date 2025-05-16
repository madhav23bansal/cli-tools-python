import argparse


def calculate_bmi(weight, height):
    """Calculates BMI given weight in kg and height in meters."""
    if height <= 0:
        return "Height must be greater than zero."
    return weight / (height**2)


def main():
    parser = argparse.ArgumentParser(description="BMI Calculator CLI")
    parser.add_argument(
        "--weight", type=float, required=True, help="Weight in kilograms (kg)"
    )
    parser.add_argument(
        "--height", type=float, required=True, help="Height in meters (m)"
    )

    args = parser.parse_args()

    bmi = calculate_bmi(args.weight, args.height)
    if isinstance(bmi, str):
        print(f"Error: {bmi}")
    else:
        print(f"Your BMI is: {bmi:.2f}")


if __name__ == "__main__":
    main()
