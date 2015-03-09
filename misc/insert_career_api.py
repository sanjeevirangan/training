#!/Python27/python


import cgi
import cgitb
import mysql_calls
import json
import sys


def insert_to_career_table():
    cgitb.enable()
    query = cgi.FieldStorage()
    sql_calls = mysql_calls.MySqlCalls()
    result = {}
    print "Content-Type: text/html\n\n"
    if "action" in query and "career_id" in query:
        if query["action"].value == "career":
            result['action'] = "CAREER"
            career_id = list(query["career_id"].value.split(','))
            sql_query = "insert ignore into career (id) values (%s)"
            sql_calls.execute_query(sql_query, career_id)
            sql_calls.commit_db()
            sql_calls.close_db()
    else:
        result['Status'] = "Invalid form key, values"
        print json.dumps(result)
        sys.exit(1)

    if sql_calls.has_errors():
        result['Status'] = "Task Completed with errors"
        result['Error-Occurrence'] = str(len(sql_calls.err_list))
        result['Errors'] = str(sql_calls.err_list)
    else:
        result['Status'] = "Task completed successfully."

    result['Task-Execution-Time'] = sql_calls.get_total_execution_time
    result['Report'] = sql_calls.response
    print json.dumps(result)

if __name__ == '__main__':
    insert_to_career_table()
