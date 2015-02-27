#!/Python27/python


# imports
import os
import cgi, cgitb
import MySQLdb
import json
from hashlib import md5
from StringIO import StringIO


def main():
    print "Content-Type: text/html\n\n"

    if os.environ['REQUEST_METHOD'].upper() == "GET":
        execute_get()
    elif os.environ['REQUEST_METHOD'].upper() == "POST":
        execute_post()
    elif os.environ['REQUEST_METHOD'].upper() == "PUT":
        execute_put()
    elif os.environ['REQUEST_METHOD'].upper() == "DELETE":
        execute_delete()
    else:
        print json.dumps({'Error': "Method '{0}' not supported".format(os.environ['REQUEST_METHOD'].upper())})


def execute_post():
    cgitb.enable()
    query = cgi.FieldStorage()
    response = {}
    if "action" in query and "username" in query and "password" in query:
        if query["action"].value == "signup":
            user_name = query["username"].value
            first_name = query["firstname"].value
            last_name = query["lastname"].value
            pwd = query["password"].value
            email = query["email_id"].value
            encrypted_pwd = md5(pwd).hexdigest()
            status = int(query["status"].value)
            address = query["address"].value
            phone = query["phone"].value

            # Create database connection
            db = MySQLdb.connect("localhost", "root", "admin", "login_test", charset='utf8')
            cursor = db.cursor()

            # Create the sql query to create the new user. If exists, update the user data.
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
                        phone = values(phone);
                        """
            sql_val_args = (user_name, first_name, last_name, email, encrypted_pwd, status, address, phone)
            try:
                cursor.execute(sql_query, sql_val_args)
                db.commit()
                # sql_result = cursor.fetchall()
            except Exception, ex:
                response['Error'] = "Database exception:{0}".format(ex.message)
            else:
                response['Result'] = 'Update success.'
            finally:
                db.close()
        else:
            response['Error'] = "Invalid value for key 'action'."
    else:
        response['Error'] = 'No form data.'
    print json.dumps(response)


def execute_get():
    cgitb.enable()
    query = cgi.FieldStorage()
    response = {}
    result = {}
    sql_result = ""
    if "action" in query and "username" in query:
        if query["action"].value == "fetch":
            user_name = query["username"].value
            # Create database connection
            db = MySQLdb.connect("localhost", "root", "admin", "login_test", charset='utf8')
            cursor = db.cursor()
            # Create the sql query to create the new user. If exists, update the user data.
            sql_query = """
                        select * from users
                        where `username` = %s ;
                        """
            sql_val_args = (user_name,)
            try:
                cursor.execute(sql_query, sql_val_args)
                sql_response = cursor.fetchall()
                if len(sql_response) >= 1:
                    sql_result = sql_response[0]
                    result['username'] = sql_result[0]
                    result['firstname'] = sql_result[1]
                    result['lastname'] = sql_result[2]
                    result['emailid'] = sql_result[3]
                    result['passwordhash'] = sql_result[4]
                    result['address'] = sql_result[5]
                    result['phone'] = sql_result[6]
                    result['status'] = sql_result[7]
                else:
                    result ['Message'] = "No records found for user: '{0}'".format(user_name)
                #print sql_result
            except Exception, ex:
                response['Error'] = "Database exception:{0}".format(ex.message)
            else:
                response['Result'] = result
            finally:
                db.close()
        else:
            response['Error'] = "Invalid value for key 'action'."
    else:
        response['Error'] = 'No form data.'
    print json.dumps(response)


def execute_put():
    cgitb.enable()
    query = cgi.FieldStorage()
    response = {}
    if "action" in query and query["action"].value == "upload":
        if "userdata-file" in query:
            file_handle = query['userdata-file']
            print file_handle
            file_object = file_handle.file
            tmp_file_object = StringIO(file_object)
            response['File-Received'] = 'Success.'
            print
            file_content = []
            file_name = os.path.basename(file_handle.filename)
            for line in file_object:
                file_content.append(line)
            response['File-content'] = file_content
            with open('resource/' + file_name, 'wb') as tmp_file:
                tmp_file.write(tmp_file_object.read())
            response['Result'] = 'Upload success.'
        else:
            response['Error'] = "No File to upload."
    else:
        response['Error'] = "Invalid value for key 'action'."
    print json.dumps(response)


def execute_delete():
    cgitb.enable()
    query = cgi.FieldStorage()
    response = {}
    result = {}
    sql_result = ""
    if "action" in query and "username" in query:
        if query["action"].value == "delete":
            user_name = query["username"].value
            # Create database connection
            db = MySQLdb.connect("localhost", "root", "admin", "login_test", charset='utf8')
            cursor = db.cursor()
            # Create the sql query to create the new user. If exists, update the user data.

            try:
                sql_query = """
                        select * from users
                        where `username` = %s ;
                        """
                sql_val_args = (user_name,)
                cursor.execute(sql_query, sql_val_args)
                sql_response = cursor.fetchall()
                print sql_response
                print user_name
                if len(sql_response) >= 1:
                    sql_query = """
                            delete from users
                            where username = %s;
                            """
                    sql_val_args = (user_name,)
                    cursor.execute(sql_query, sql_val_args)
                    #sql_response = cursor.fetchall() # This gives no meaningful info
                    db.commit()

                    sql_query = """
                        select * from users
                        where `username` = %s ;
                        """
                    sql_val_args = (user_name,)
                    cursor.execute(sql_query, sql_val_args)
                    sql_response = cursor.fetchall()
                    if len(sql_response) >= 1:
                        result['Failure'] = "Record NOT deleted for user: {0}".format(user_name)
                    else:
                        result['Success'] = "Record deleted for user: {0}".format(user_name)
                else:
                    result['Error'] = "No records found for user: {0}".format(user_name)
            except Exception, ex:
                response['Error'] = "Database exception:{0}".format(ex.message)
            else:
                response['Result'] = result
            finally:
                db.close()
        else:
            response['Error'] = "Invalid value for key 'action'."
    else:
        response['Error'] = 'No form data.'
    print json.dumps(response)


main()