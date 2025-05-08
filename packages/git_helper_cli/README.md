# Git Helper CLI

A simple CLI tool to quickly get help with common Git commands.

## Installation

To install this tool, navigate to the `packages/git_helper_cli` directory and run:

```bash
pip install .
```

Alternatively, for development mode:

```bash
pip install -e .
```

## Usage

Once installed, you can use the `git_helper` command in your terminal.

### List all available commands:

```bash
git_helper --list
```

### Get help for a specific command:

```bash
git_helper <command_name>
```

Example:

```bash
git_helper clone
```

This will display the description, usage, and an example for the `git clone` command.

## Supported Commands

Currently, the tool supports help for the following Git commands:

- clone
- init
- add
- commit
- status
- branch
- checkout
- merge
- pull
- push
- remote
- log
- diff
- reset
- stash
