# Random Password Generator CLI

A simple command-line tool to generate random passwords.

## Installation

To install the tool, navigate to the `packages/random_password_generator_cli` directory and run:

```bash
pip install .
```

## Usage

Once installed, you can use the tool from your terminal:

```bash
random_password --length <number_of_characters>
```

### Options

- `--length`: Specifies the length of the password. Defaults to 12 if not provided.

### Example

To generate a password of length 16:

```bash
random_password --length 16
```

This will output a randomly generated password of 16 characters.
