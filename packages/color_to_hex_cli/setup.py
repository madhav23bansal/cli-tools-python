from setuptools import setup, find_packages

setup(
    name="color-to-hex-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "color_to_hex_cli=color_to_hex_cli.main:main",
        ],
    },
    install_requires=[
        "typer[all]",  # typer[all] includes rich for nice printing
        "webcolors",
    ],
)
