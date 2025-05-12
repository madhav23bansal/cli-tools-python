from setuptools import setup, find_packages

setup(
    name="simple-calculator-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "simple-calculator = simple_calculator_cli.main:cli",
        ],
    },
    author="Cline",
    author_email="cline@example.com",
    description="A simple CLI calculator supporting addition and multiplication.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/simple-calculator-cli",  # Replace with your actual URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
