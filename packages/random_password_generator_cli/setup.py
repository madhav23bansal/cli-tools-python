from setuptools import setup, find_packages

setup(
    name="random_password_generator_cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "random_password=random_password_generator_cli.main:main",
        ],
    },
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A CLI tool to generate random passwords.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/random_password_generator_cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
