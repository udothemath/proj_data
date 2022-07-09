
SELECT {%
for var in table2.query.variable %}
    {{var.varname}},{% endfor %}
    1 as dummy
FROM "{{schema}}.{{table1.tablename}}"
