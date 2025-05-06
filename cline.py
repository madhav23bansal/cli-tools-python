# cline.py

import ast
import inspect


def extract_args_from_function(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    func_def = tree.body[0]

    args = []
    for arg in func_def.args.args:
        args.append(arg.arg)
    return args


# Test function
def sample_function(name: str, age: int, active: bool = True):
    pass


def main():
    print("Welcome to cline - The CLI Generator Tool")
    args = extract_args_from_function(sample_function)
    print("Extracted args:", args)


if __name__ == "__main__":
    main()
