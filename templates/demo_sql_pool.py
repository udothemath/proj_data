sql_v7 = ''' 
-- Comments: {{table3.comment}} 
SELECT {%
for _, value in table3.variable.items
() %}
    {{value}},{% endfor %}
    1 as dummy
FROM "{{schema}}.{{table3.tablename}}"
'''
sql_v8 = ''' 
-- Comments: Left join
SELECT {%for _, value in table3.variable.items() %}
    {{table3.tablename_as}}.{{value}},{% endfor %}
    {{table4.tablename_as}}.{{table3.variable.varname1}}
    {{table4.condition.cond1}}({{table4.tablename_as}}.{{table4.variable.varname2}}) AS total_spent
FROM {{schema}}.{{table3.tablename}} {{table3.tablename_as}}
LEFT JOIN {{schema}}.{{table4.tablename}} {{table4.tablename_as}}
ON {{table3.tablename_as}}.{{table3.variable.varname1}} = {{table4.tablename_as}}.{{table4.variable.varname1}}
GROUP BY {{table3.tablename_as}}.{{table3.variable.varname1}}
'''
