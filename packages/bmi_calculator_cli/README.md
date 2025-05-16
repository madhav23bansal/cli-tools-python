# BMI Calculator CLI

A simple command-line tool to calculate Body Mass Index (BMI).

## Installation

To install the BMI Calculator CLI, navigate to the `packages/bmi_calculator_cli` directory and run:

```bash
pip install .
```

Alternatively, if you want to install it in editable mode (useful for development):

```bash
pip install -e .
```

## Usage

Once installed, you can use the `bmi-calculator` command from your terminal:

```bash
bmi-calculator --weight <weight_in_kg> --height <height_in_meters>
```

### Arguments

- `--weight`: Your weight in kilograms (e.g., 70).
- `--height`: Your height in meters (e.g., 1.75).

### Example

```bash
bmi-calculator --weight 70 --height 1.75
```

This will output:

```
Your BMI is: 22.86
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
