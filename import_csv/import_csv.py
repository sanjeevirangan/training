import sys
import csv
import MySQLdb
from validate_email_address import validate_email

'''
Imports the csv file and updates the fields to database.
Fields required:
++++++++++++++++++++++
username
firstname
lastname
passwordhash
status
email
address
phone
++++++++++++++++++++++
'''


def main():
    csv_file = sys.argv[1]
    #user_dict = {}  # Store user data to validate and process
    try:
        db = MySQLdb.connect("localhost", "root", "admin", "login_test", charset='utf8')
    except Exception, ex:
        print("Fatal Error: Unable to connect to database.\n{0}".format(ex.message))
        sys.exit(1)

    cursor = db.cursor()
    sql_query = """insert ignore into users
               (username, firstname, lastname, emailid, passwordhash, status, address, phone)
                values (%s,%s,%s,%s,%s, %s, %s, %s)"""
    sql_val_args = ""

    # start reading the file
    print("\nReading file {0}\n".format(csv_file))
    print"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    with open(csv_file, 'r') as file_handle:
        dict_reader = csv.DictReader(file_handle)
        for row in dict_reader:
            '''
            # A dictionary that has a inner dictionary of all data for each user entry found in the file.
            user_dict[row['username']] = dict(username=row['username'],
                                              firstname=row['firstname'],
                                              lastname=row['lastname'],
                                              passwordhash=row['passwordhash'],
                                              status=row['status'],
                                              email=row['email'],
                                              address=row['address'],
                                              phone=row['phone'].replace(" ", "")
            '''
            # Make a database entry only for valid records
            user = row['username']
            email_id = row['email'].replace(" ", "")
            phone_num = row['phone'].replace(" ", "")
            print("Validating user record for user: {0}\n".format(user))
            if validate_user_data(email_id, phone_num):
                sql_val_args = (user, row['firstname'], row['lastname'],
                                email_id, row['passwordhash'], int((row['status'])),
                                row['address'], phone_num)
                print("Executing database entry...\n")
                try:
                    cursor.execute(sql_query, sql_val_args)
                except Exception, ex:
                    print("Error: An error occurred while updating database\n{0}".format(ex.message))
                else:
                    print("Updated database entry for user: {0}".format(user))
            else:
                print("Error: Invalid record found.\n")
                if 'username' in row:
                    print("Skipping import process for record: '{0}'\n".format(row['username']))
                else:
                    print("Skipping import process for line: '{0}'\n".format(dict_reader.line_num))
            print "______________________________________________________\n"
    try:
        db.commit()
        print("Import process completed successfully...\n")
        print"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        sql_result = cursor.fetchall()
    finally:
        db.close()


'''
Validates email id and phone number.
For MX check and verification of email, network should send the DNS response to host machine.
'''


def validate_user_data(email, phone):
    res = False
    if validate_email(email) and phone.isdigit():
        res = True
    return res


main()
