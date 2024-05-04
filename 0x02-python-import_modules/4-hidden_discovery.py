#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    import os

# Check if the compiled module exists
if not os.path.isfile('hidden_4.pyc'):
    print("Error: The compiled module 'hidden_4.pyc' does not exist.")
    exit()

# Load the compiled module
spec = importlib.util.spec_from_file_location(
    'hidden_4', 'hidden_4.pyc')
hidden_4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden_4)

# Print the names in alpha order, excluding names starting with '__'
for name in sorted(dir(hidden_4)):
    if not name.startswith('__'):
        print(name)
