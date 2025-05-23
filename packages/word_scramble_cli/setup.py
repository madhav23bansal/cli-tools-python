from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="word-scramble-cli",
    version="0.1.0",
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A CLI Word Scramble game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/word_scramble_cli",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "word_scramble=word_scramble_cli.main:play",
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
