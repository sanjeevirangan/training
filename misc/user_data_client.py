import argparse
import requests
import json
import sys


def main():
    payload = {}
    parser = argparse.ArgumentParser()
    #parser.add_argument("--url", "-u", required=True)
    parser.add_argument("--action", "-a", required=True, default='signup')
    parser.add_argument("--username", "-un")
    parser.add_argument("--password", "-pwd")
    parser.add_argument("--firstname", "-fn")
    parser.add_argument("--lastname", "-ln")
    parser.add_argument("--emailid", "-e")
    parser.add_argument("--status", "-s")
    parser.add_argument("--address", "-ad")
    parser.add_argument("--phone", "-p")
    parser.add_argument("--file", "-f")
    args = parser.parse_args()

    if args.action is not None:
        payload['action'] = args.action
    if args.username is not None:
        payload['username'] = args.username.strip()
    if args.password is not None:
        payload['password'] = args.password
    if args.firstname is not None:
        payload['firstname'] = args.firstname
    if args.lastname is not None:
        payload['lastname'] = args.lastname
    if args.emailid is not  None:
        payload['email_id'] = args.emailid
    if args.status is not None:
        payload['status'] = args.status
    if args.address is not None:
        payload['address'] = args.address
    if args.phone is not None:
        payload['phone'] = args.phone
    if args.file is not None:
        payload['userdata-file'] = file(args.file, 'r')

    #headers = {'content-type': 'application/json'}
    #headers = {'content-type': 'application/text'}
    #headers = {'content-type': 'application/form-data'}

    url = 'http://localhost/cgi-bin/api/user-data-api.py'
    '''
    The content type should be 'x-www-form-urlencoded'. If not specified, the cgi wont read the field storage correctly.
    '''
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    if payload['action'] == 'signup':
        if 'username' in payload and 'password' in payload:
            r = requests.post(url, data=payload, headers=headers)
            print r.text
        else:
            print "\nError: Username or password not mentioned."
            sys.exit(1)
    elif payload['action'] == 'fetch':
        if 'username' in payload:
            url += "?action=fetch&username={0}".format(payload['username'])
            print url
            r = requests.get(url.strip("'"))
            print r.text
        else:
            print "\nError: Username not mentioned."
            sys.exit(1)
    elif payload['action'] == 'upload':
        #headers = {'content-type': 'application/form-data'}
        if 'userdata-file' in payload:
            r = requests.put(url, data=payload)
            print r.text
        else:
            print "\nError: No file to upload."
            sys.exit(1)
    elif payload['action'] == 'delete':
        if 'username' in payload:
            r = requests.delete(url, data=payload)
            print r.text
        else:
            print "\nError: Username not mentioned."
            sys.exit(1)

main()