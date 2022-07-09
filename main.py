# %%
from demo_jinja import quick_demo_jinja1, quick_demo_jinja2
from demo_yaml import quick_demo_yaml1, quick_demo_yaml2, quick_demo_yaml3

if __name__ == "__main__":
    print(" ==== Start ==== ")
    j1 = quick_demo_jinja1()
    j2 = quick_demo_jinja2()
    # print(j1)
    # print(j2)

    file_yaml = 'demo_yaml_file.yml'
    yaml1 = quick_demo_yaml1(filename=file_yaml)
    yaml2 = quick_demo_yaml2(filename=file_yaml)
    # print(yaml1)
    # print(yaml2)

    file_html = 'demo_html.html'
    yaml3 = quick_demo_yaml3(vars=yaml1, filename=file_html)
    # print(yaml3)

    file_yaml_for_sql = 'demo_yaml_sql.yml'
    var = quick_demo_yaml1(filename=file_yaml_for_sql)
    file_sql = 'demo_sql_v1.sql'
    result4 = quick_demo_yaml3(vars=var, filename=file_sql)
    # print(result4)

    file_yaml_for_sql = 'demo_yaml_sql.yml'
    var = quick_demo_yaml1(filename=file_yaml_for_sql)
    file_sql = 'demo_sql_v2.sql'
    result5 = quick_demo_yaml3(vars=var, filename=file_sql)
    # print(result5)

    file_yaml_for_sql = 'demo_yaml_sql.yml'
    var = quick_demo_yaml1(filename=file_yaml_for_sql)
    file_sql = 'demo_sql_v3.sql'
    result6 = quick_demo_yaml3(vars=var, filename=file_sql)
    print(result6)

    print(" ==== End ==== ")
