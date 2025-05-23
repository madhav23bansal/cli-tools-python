import os
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
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A CLI tool to convert color names to hex codes.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/color_to_hex_cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
