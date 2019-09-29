def query_builder(query, query_vars):
    query_var_list = []
    for key, value in query_vars.items():
        query_var_list.append('{}={}'.format(key, value))

    return query + '?' + '&'.join(query_var_list)
