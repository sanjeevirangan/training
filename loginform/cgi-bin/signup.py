#!/Python27/python

# imports
import cgi, MySQLdb
from hashlib import md5


def main():
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("username") and form.has_key("password")):
        if (form["action"].value == "signup"):
            id = form["username"].value
            first_name = form["firstname"].value
            last_name = form["lastname"].value
            pwd = form["password"].value
            repeat_pwd = form["repeat_password"].value
            if len(id) > 5 and pwd == repeat_pwd:
                email = form["email_id"].value
                encrypted_pwd = md5(pwd).hexdigest()
                db = MySQLdb.connect("localhost", "root", "admin", "login_test", charset='utf8')
                cursor = db.cursor()
                sql_query = """insert ignore into users
                                   (username, firstname, lastname, emailid, passwordhash) values (%s,%s,%s,%s,%s)"""
                sql_val_args = (id, first_name, last_name, email, encrypted_pwd)
                try:
                    cursor.execute(sql_query, sql_val_args)
                    db.commit()
                    sql_result = cursor.fetchall()
                finally:
                    db.close()
                print 'Location: http://localhost/loginform/signedup.html\n'
            else:
                print "Location: http://localhost/loginform/error.html\n"
    else:
        print "Location: http://localhost/loginform/error.html\n"

main()