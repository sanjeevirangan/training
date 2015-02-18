#!/Python27/python

# imports
import cgi, MySQLdb
from hashlib import md5

# Function to generate HTML login form.
def load_login_form(msg):
    print "Content-Type: text/html"
    print
    print """
    <TITLE>Login form</TITLE>
    <H1>Login to proceed</H1>
    """
    print "\t<H3>{0}</H3>\n".format(msg)
    print "\t<TABLE BORDER = 0>\n"

    print "\t\t<FORM METHOD = post ACTION = '/cgi-bin/loginform/index.py'>\n"
    print "\t\t<TR><TH>Username:</TH><TD><INPUT TYPE = text NAME = 'username'></TD><TR>\n"
    print "\t\t<TR><TH>Password:</TH><TD><INPUT TYPE = password NAME = 'password'></TD></TR>\n"
    print "\t</TABLE>\n"

    print "\t<INPUT TYPE = hidden NAME = 'action' VALUE = 'display'>\n"
    print "\t<INPUT TYPE = submit VALUE = 'Enter'>\n"

    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

#load_login_form()


def load_welcome_page(id):
    print "Content-Type: text/html"
    print
    print """
    <TITLE>Weldome</TITLE>
    <H1>Welcome to awesome page!!!</H1>
    """
    print "\t<H3>Howdy, {0}</H3>\n".format(id)


def load_error_page():
    print "Content-Type: text/html"
    print
    print """
    <TITLE>Error</TITLE>
    <H1>Something went wrong :(</H1>
    """

	
def authenticate_dict(id, pwd):
    pwd_dict = {'sanjeevi':'7f336b23fccd6042a5cf5a5bdaffd40f', 
		'abc': '900150983cd24fb0d6963f7d28e17f72',
		'ravi' : '63dd3e154ca6d948fc380fa576343ba6' }
    result = False

    if id in pwd_dict.keys():
        dict_Password = pwd_dict[id]
        if pwd == dict_Password:
            result = True

    return result


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
            if pwd == db_pwd_hash :
                result = True        
    finally:
        db.close()

    return result


def main():
    form_message = "Please enter your username and password."
    error_message = "Invalid credentials!!!!\n\nPlease try again.."
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("username") and form.has_key("password")):
        if (form["action"].value == "display"):
            id = form["username"].value
            pwd = form["password"].value
            encrypted_pwd = md5(pwd).hexdigest()  
            if authenticate_db(id,encrypted_pwd):
                load_welcome_page(id)
            else:
	        #print "Invalid ID"
    		load_login_form(error_message)
    else:
        load_login_form(form_message)
 
main()
    
