from setuptools import setup

setup(
    name="git_helper_cli",
    version="0.1.0",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "git_helper = main:main",
        ],
    },
    author="Madhav Bansal",
    author_email="madhavb.dev@gmail.com",
    description="A CLI tool to get help with Git commands.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/madhav23bansal/cli-tools-python/tree/main/packages/git_helper_cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
