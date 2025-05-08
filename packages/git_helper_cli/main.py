import argparse


def show_git_help(command_name=None):
    """
    Displays help information for Git commands.
    """
    git_commands = {
        "clone": {
            "description": "Clone a repository into a new directory.",
            "usage": "git clone <repository_url>",
            "example": "git clone https://github.com/user/repo.git",
        },
        "init": {
            "description": "Create an empty Git repository or reinitialize an existing one.",
            "usage": "git init",
            "example": "git init",
        },
        "add": {
            "description": "Add file contents to the index (staging area).",
            "usage": "git add <file_path_or_pattern>",
            "example": "git add . (adds all changes)\ngit add README.md (adds a specific file)",
        },
        "commit": {
            "description": "Record changes to the repository.",
            "usage": 'git commit -m "<commit_message>"',
            "example": 'git commit -m "Initial commit"',
        },
        "status": {
            "description": "Show the working tree status.",
            "usage": "git status",
            "example": "git status",
        },
        "branch": {
            "description": "List, create, or delete branches.",
            "usage": "git branch (lists branches)\ngit branch <branch_name> (creates a new branch)\ngit branch -d <branch_name> (deletes a branch)",
            "example": "git branch feature/new-login\ngit branch -d old-feature",
        },
        "checkout": {
            "description": "Switch branches or restore working tree files.",
            "usage": "git checkout <branch_name>\ngit checkout -b <new_branch_name> (creates and switches to a new branch)",
            "example": "git checkout main\ngit checkout -b develop",
        },
        "merge": {
            "description": "Join two or more development histories together.",
            "usage": "git merge <branch_name>",
            "example": "git checkout main\ngit merge develop",
        },
        "pull": {
            "description": "Fetch from and integrate with another repository or a local branch.",
            "usage": "git pull <remote_name> <branch_name>",
            "example": "git pull origin main",
        },
        "push": {
            "description": "Update remote refs along with associated objects.",
            "usage": "git push <remote_name> <branch_name>",
            "example": "git push origin main",
        },
        "remote": {
            "description": "Manage set of tracked repositories.",
            "usage": "git remote -v (list remotes)\ngit remote add <name> <url> (add a new remote)",
            "example": "git remote add upstream https://github.com/original_author/repo.git",
        },
        "log": {
            "description": "Show commit logs.",
            "usage": "git log",
            "example": "git log --oneline --graph --decorate",
        },
        "diff": {
            "description": "Show changes between commits, commit and working tree, etc.",
            "usage": "git diff\ngit diff <commit_hash>\ngit diff <branch1>..<branch2>",
            "example": "git diff HEAD^\ngit diff main..develop",
        },
        "reset": {
            "description": "Reset current HEAD to the specified state.",
            "usage": "git reset <mode> <commit>\ngit reset --hard HEAD (discard all local changes)\ngit reset --soft HEAD^ (undo last commit, keep changes staged)",
            "example": "git reset --hard origin/main",
        },
        "stash": {
            "description": "Stash the changes in a dirty working directory away.",
            "usage": "git stash\ngit stash pop\ngit stash list",
            "example": 'git stash save "WIP: login form"\ngit stash apply stash@{0}',
        },
    }

    if command_name:
        command = git_commands.get(command_name.lower())
        if command:
            print(f"Command: git {command_name}")
            print(f"  Description: {command['description']}")
            print(f"  Usage: {command['usage']}")
            # Prepare example text, replacing newlines for proper indentation
            example_text = command["example"].replace("\n", "\n    ")
            print(f"  Example(s):\n    {example_text}")
        else:
            print(f"Error: Command 'git {command_name}' not found.")
            print("Use 'git_helper --list' to see all available commands.")
    else:
        print("Git Command Helper")
        print("Usage: git_helper <command_name>")
        print("   or: git_helper --list")
        print("\nAvailable commands:")
        for cmd in git_commands.keys():
            print(f"  - {cmd}")
        print(
            "\nFor detailed help on a specific command, type: git_helper <command_name>"
        )


def main():
    parser = argparse.ArgumentParser(description="Git Command Helper CLI")
    parser.add_argument(
        "command_name",
        nargs="?",
        help="The Git command to get help for (e.g., clone, commit, branch).",
    )
    parser.add_argument(
        "--list", action="store_true", help="List all available Git commands."
    )

    args = parser.parse_args()

    if args.list:
        show_git_help()
    elif args.command_name:
        show_git_help(args.command_name)
    else:
        show_git_help()


if __name__ == "__main__":
    main()
