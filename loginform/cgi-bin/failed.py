#!/Python27/python

# imports
import cgi


def main():
    form = cgi.FieldStorage()
    username = form["user"].value
    print "Content-Type: text/html"
    print """
    <HTML>
    <BODY>
    <TITLE>Login Failed</TITLE>
    <H1>Login Failed!!!</H1>
    <H2>The login attempt for the user: </H2><H2 style="color:red">{0}<H2>
    <H2>is failed.. </H2>
    <form action= 'http://localhost/loginform/index.html'>
      <input type="submit" value="Re-try">
    </form>
    </BODY>
    </HTML> """.format(username)


main()