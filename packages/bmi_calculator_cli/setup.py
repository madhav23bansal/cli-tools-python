from setuptools import setup, find_packages

setup(
    name="bmi_calculator_cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bmi-calculator=bmi_calculator_cli.main:main",
        ],
    },
    install_requires=[],
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A simple CLI tool to calculate BMI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/bmi_calculator_cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
