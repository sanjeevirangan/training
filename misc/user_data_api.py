#!/Python27/python

# imports
import os
import cgi, cgitb
import MySQLdb
import json
from hashlib import md5


def main():
    print "Content-Type: text/html\n"

    if os.environ['REQUEST_METHOD'] == "GET":
        execute_get()
    elif os.environ['REQUEST_METHOD'] == "POST":
        execute_post()


def execute_post():
    cgitb.enable()
    query = cgi.FieldStorage()
    print type(query)
    print query
    #print json.dumps({'query': str(query)})
    if "action" in query and "username" in query and "password" in query:
        if query["action"].value == "signup":
            id = query["username"].value
            #repeat_pwd = query["repeat_password"].value
            if len(id) > 5: # and pwd == repeat_pwd:
                first_name = query["firstname"].value
                last_name = query["lastname"].value
                pwd = query["password"].value
                email = query["email_id"].value
                encrypted_pwd = md5(pwd).hexdigest()
                status = int(query["status"].value)
                address = query["address"].value
                phone = query["phone"].value

                db = MySQLdb.connect("localhost", "root", "admin", "login_test", charset='utf8')
                cursor = db.cursor()
                sql_query = """
                    insert into users
                    (username, firstname, lastname, emailid, passwordhash, status, address, phone)
                    values (%s,%s,%s,%s,%s, %s, %s, %s)
                    on duplicate key update
                    firstname = values(firstname),
                    lastname = values(lastname),
                    emailid = values(emailid),
                    passwordhash = values(passwordhash),
                    status = values(status),
                    address = values(address),
                    phone = values(phone)"""
                sql_val_args = (id, first_name, last_name, email, encrypted_pwd, status, address, phone)
                try:
                    cursor.execute(sql_query, sql_val_args)
                    db.commit()
                    # sql_result = cursor.fetchall()
                finally:
                    db.close()
                print json.dumps({'Result': 'Update success'})
            else:
                print json.dumps({'Error': 'Invalid user name or password mismatch'})
    else:
        print json.dumps({'Error': 'No form data'})


def execute_get():
    print json.dumps({'Result': 'Nothing to get'})


main()
