#!/usr/bin/python3
# Prints all the names defined by the compiled module "hidden_4.pyc"
if __name__ == "__main__":
    import hidden_4

    modules = dir(hidden_4)
    for module in modules:
        if module[:2] != "__":
            print(module)
