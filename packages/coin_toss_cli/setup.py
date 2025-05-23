from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="coin-toss-cli",
    version="0.1.0",
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A CLI Coin Toss Simulator with rich UI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/coin_toss_cli",
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "coin_toss=coin_toss_cli.main:toss",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Assuming MIT License
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",  # Prod-ready implies Beta or higher
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: Terminals",
    ],
    python_requires=">=3.6",
)
