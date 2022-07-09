from jinja2 import Template


def quick_example1():
    t = Template("Hello {{ something }}!")
    msg = t.render(something="World")
    print(msg)


def quick_example2():
    t = Template(
        "My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
    msg = t.render()
    print(msg)
