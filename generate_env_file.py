import os
import ast

# Path to the config.py file
CONFIG_FILE = "config.py"
OUTPUT_ENV_FILE = ".env"

def extract_uppercase_variables(file_path):
    """Extract all uppercase variables from a Python file."""
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    variables = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper():
                    variables[target.id] = node.value.s if isinstance(node.value, ast.Constant) else ""
    return variables

def read_env_file(file_path):
    """Read existing .env file and return its variables as a dictionary."""
    if not os.path.exists(file_path):
        return {}

    env_vars = {}
    with open(file_path, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                env_vars[key] = value
    return env_vars

def write_env_file(variables, output_path):
    """Write variables to a .env file, appending new ones if the file exists."""
    existing_vars = read_env_file(output_path)

    with open(output_path, "a" if existing_vars else "w") as file:
        if existing_vars:
            file.write("\n")  # Ensure a new line is added at the end of old content
        for key, value in variables.items():
            if key not in existing_vars:
                file.write(f"{key}={value}\n")

def main():
    # Extract variables from config.py
    variables = extract_uppercase_variables(CONFIG_FILE)

    # Write or update .env file
    write_env_file(variables, OUTPUT_ENV_FILE)
    print(f".env file updated with {len(variables)} entries.")

if __name__ == "__main__":
    main()