from yaml import safe_load


def quick_demo_yaml1():
    filename = 'demo_yaml_file.yml'
    with open(filename, 'r') as f:
        vars_string = f.read()
    base_vars = safe_load(vars_string)
    print(base_vars)
