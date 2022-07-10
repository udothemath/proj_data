# from typing import Any, Type
from jinja2 import Environment, FileSystemLoader, Template
from yaml import safe_load


def quick_demo_yaml1(filename: str) -> str:
    with open(filename, 'r') as f:
        vars_string = f.read()
    base_vars = safe_load(vars_string)
    return base_vars


def quick_demo_yaml2(filename: str) -> str:
    with open(filename, 'r') as f:
        vars_string = f.read()
    base_vars = safe_load(vars_string)
    parsed_yaml = Template(vars_string).render(base_vars)
    return parsed_yaml


def quick_demo_yaml3(vars: str, filename: str) -> str:
    load = FileSystemLoader('templates')
    env = Environment(loader=load)
    template = env.get_template(filename)
    result = template.render(vars)
    return result


def quick_demo_yaml4() -> str:
    vars_string = '''
        SELECT {% for _, value in table3.variable.items() %}
            {{value}},{% endfor %}
            1 as dummy
        FROM "{{schema}}.{{table3.tablename}}"   
    '''
    jinja = Environment(loader=FileSystemLoader(
        '.'), trim_blocks=True, lstrip_blocks=True)
    template = jinja.get_template(vars_string)
    print(template)
    # yaml=YAML()
    # yaml.allow_duplicate_keys = True
    # yaml.explicit_start = True
    # yaml_content = yaml.load(template.render())
    # print (yaml_content['package'])

    # base_vars = safe_load(vars_string)
    # parsed_yaml = Template(base_vars).render()
    # print(base_vars)
    # print(parsed_yaml)

    # return parsed_yaml
