#!/Python27/python


import cgi
import cgitb
import MySQLdb
import my_response
import sys


def insert_to_career_product_table():
    cgitb.enable()
    query = cgi.FieldStorage()

    body = {}
    headers = {"Content-Type": "application/json",
               "API": "Insert to 'CAREER_PRODUCT' table",
               "author": "sanjeevi rangan",
               "contact": "sanjeevirangan@gmail.com"}
    body['Is_Error'] = 'False'
    response = my_response.MyResponse()
    response.status_code = 500

    if "action" in query and "weight" in query and "career_id" in query and "product_id" in query:
        if query["action"].value.lower() == "career_product":
            body['action'] = "CAREER_PRODUCT"
            weight = query["weight"].value
            career_id = query["career_id"].value
            product_id = query["product_id"].value
            sql_query = "insert ignore into career_product (weight, career_id, product_id) values (%s, %s, %s)"
            try:
                db = MySQLdb.connect("localhost", "root", "admin", "product_relation", charset='utf8')
                cursor = db.cursor()
            except Exception, ex:
                response.status_code = 503
                body['Error'] = "Database exception:{0}".format(ex.message)
                body['Is_Error'] = 'True'
                body['Result'] = "Failed to insert {0}, {1}, {2}".format(weight, career_id, product_id)
                response.write()
                sys.exit(1)
            try:
                cursor.execute(sql_query, (weight, career_id, product_id))
                db.commit()
            except Exception, ex:
                response.status_code = 400
                body['Error'] = "Error while executing query:{0}".format(ex.message)
                body['Is_Error'] = 'True'
                body['Result'] = "Failed to insert {0}, {1}, {2}".format(weight, career_id, product_id)
            else:
                response.status_code = 200  # OK
                body['Result'] = "Successfully inserted {0}, {1}, {2}".format(weight, career_id,product_id)
            #  Done with DB
            db.close()
        else:
            response.status_code = 400
            body['Is_Error'] = 'True'
            body['Error'] = "Invalid value for key 'action'."
    else:
        response.status_code = 400
        body['Is_Error'] = 'True'
        body['Error'] = 'No form data.'

    response.headers = headers

    response.body = body
    response.write()

if __name__ == '__main__':
    insert_to_career_product_table()