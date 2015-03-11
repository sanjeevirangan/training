from flask import Flask, request
from flask import render_template
import MySQLdb
from hashlib import md5


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login():
    #print str(request.form)
    #return "You will be logged in soon"
    username = request.form['username']
    password = request.form['password']
    #return username, password
    try:
        db = MySQLdb.connect("localhost", "root", "admin", "login_test")
        cursor = db.cursor()
    except Exception, ex:
        return "Database Error: {0}".format(ex.message)
    sql_query = "select passwordhash, firstname, lastname from users where username = '{0}'".format(username)
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
    except Exception, ex:
        return "Error while querying database: {0}".format(ex.message)
    finally:
        db.close()
    if len(result) > 0:
        db_pwd_hash = result[0][0]
        if db_pwd_hash == md5(password).hexdigest():
            db_first_name = result[0][1]
            db_last_name = result[0][2]
            user = {'firstname': db_first_name,
                    'lastname': db_last_name}
            page = {'title': 'Welcome',
                    'message': 'Welcome to this awesome page!'}
            return render_template('welcome.html', user=user, page=page)
    return render_template('invalid.html')


@app.route('/create-profile', methods=['POST'])
def create_profile():
    #return "i need to sleep now. Let me do it tomorrow."
    username = request.form["username"]
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    password = request.form["password"]
    repeat_password = request.form["repeat_password"]

    if len(username) > 5 and password == repeat_password:
        email = request.form["email_id"]
        encrypted_pwd = md5(password).hexdigest()
        try:
            db = MySQLdb.connect("localhost", "root", "admin", "login_test")
            cursor = db.cursor()
        except Exception, ex:
            return "Database Error: {0}".format(ex.message)
        sql_query = """insert into users
                       (username, firstname, lastname, emailid, passwordhash) values (%s,%s,%s,%s,%s)
                       on duplicate key update
                       username = values(username), firstname = values(firstname), lastname = values(lastname),
                       emailid = values(emailid), passwordhash = values(passwordhash)"""
        sql_val_args = (username, first_name, last_name, email, encrypted_pwd)
        try:
            cursor.execute(sql_query, sql_val_args)
            db.commit()
        finally:
            db.close()
        return "Profile creation successfully"
    else:
        return render_template('error.html')



if __name__ == "__main__":
    app.run(debug=True)
