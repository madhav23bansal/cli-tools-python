from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hangman-game-cli",
    version="0.1.0",
    author="Cline",  # Assuming Cline is the author, can be changed
    author_email="cline@example.com",  # Placeholder email
    description="A CLI Hangman game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cline/tree/main/packages/hangman_game_cli",  # Placeholder URL
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "hangman_game=hangman_game_cli.main:play",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Assuming MIT License
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.6",
)
