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
    author="Cline",
    author_email="cline@example.com",
    description="A CLI tool to get help with Git commands.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/git_helper_cli",  # Replace with actual URL if available
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
