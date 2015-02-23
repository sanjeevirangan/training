#!/Python27/python

# imports
import cgi,MySQLdb
from hashlib import md5


def authenticate_db(id, pwd):
    db = MySQLdb.connect("localhost","root","admin","login_test" )
    cursor = db.cursor()
    sql_query = "select passwordhash from users where username = '{0}'".format(id)
    result = False
    try:
        cursor.execute(sql_query)
        sql_result = cursor.fetchall()
        if len(sql_result) > 0:
            db_pwd_hash = sql_result[0][0]
            if pwd == db_pwd_hash:
                result = True
    finally:
        db.close()

    return result


def main():
    form = cgi.FieldStorage()
    if form.has_key("action") and form.has_key("username") and form.has_key("password"):
        if form["action"].value == "display":
            id = form["username"].value
            pwd = form["password"].value
            encrypted_pwd = md5(pwd).hexdigest()
            if authenticate_db(id,encrypted_pwd):
                print 'Location: http://localhost/loginform/welcome.html\n'
            else:
                print "Location: http://localhost/cgi-bin/loginform/failed.py?user={0}\n".format(id)
    else:
        print "Location: http://localhost/loginform/invalid.html\n"

main()