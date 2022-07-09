sql_a = ''' 
        -- Comments: {{table3.comment}} 
        SELECT {%
        for _, value in table3.variable.items
        () %}
            {{value}},{% endfor %}
            1 as dummy
        FROM "{{schema}}.{{table3.tablename}}"
    '''
