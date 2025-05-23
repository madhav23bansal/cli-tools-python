from setuptools import setup, find_packages

setup(
    name="countdown_timer_cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # No external dependencies for now
    ],
    entry_points={
        "console_scripts": [
            "countdown_timer=countdown_timer_cli.main:main",
        ],
    },
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A simple countdown timer CLI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/countdown_timer_cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
