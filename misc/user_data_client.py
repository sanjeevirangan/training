import argparse
import requests
import json


def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--url", "-u", required=True)
    parser.add_argument("--action", "-a", required=True, default='signup')
    parser.add_argument("--username", "-un", required=True)
    parser.add_argument("--password", "-pwd", required=True)
    parser.add_argument("--firstname", "-fn")
    parser.add_argument("--lastname", "-ln")
    parser.add_argument("--emailid", "-e")
    parser.add_argument("--status", "-s")
    parser.add_argument("--address", "-ad")
    parser.add_argument("--phone", "-p")
    args = parser.parse_args()

    payload = dict(action=args.action, username=args.username, password=args.password, firstname=args.firstname,
                   lastname=args.lastname, email_id=args.emailid, status=args.status, address=args.address,
                   phone=args.phone)
    #headers = {'content-type': 'application/json'}
    headers = {'content-type': 'application/text'}
    #url = str(args.url)
    url = 'http://localhost/cgi-bin/api/post-user-data.py'
    r = requests.post(url, payload, headers=headers)

    print r.text


main()
