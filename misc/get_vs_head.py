import requests
import time
import argparse


def check_requests():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-u", help="url to test", default="http://httpbin.org/get")
    args = parser.parse_args()
    url = args.url

    head_start = time.time()
    h = requests.head(url)
    head_end = time.time()
    time_head = head_end - head_start
    print "---------------------------------------------------------"
    print "Time taken by 'requests.head': {0} seconds".format(time_head)
    print "---------------------------------------------------------"
    print "head.headers()\n"
    print h.headers

    get_start = time.time()
    g = requests.get(url)
    get_end = time.time()
    time_get = get_end - get_start
    print "---------------------------------------------------------"
    print "Time taken by 'requests.get': {0} seconds".format(str(time_get))
    print "---------------------------------------------------------"
    print "get.headers()\n"
    print g.headers
    print
    print "----------------------------------------------------------------------------"
    print "Time difference between 'head' and 'get' methods: {0} seconds".format(str(time_get -time_head))
    print "----------------------------------------------------------------------------"


check_requests()
