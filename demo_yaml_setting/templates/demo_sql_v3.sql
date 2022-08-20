-- Comments: {{table2.comment}} 
SELECT {% for var in table2.query.variable %}
    {{var.varname}},{% endfor %}
    1 as dummy
FROM "{{schema}}.{{table2.tablename}}"
WHERE 
{{table2.query.condition.condition1}}
AND  
{{table2.query.condition.condition2}}