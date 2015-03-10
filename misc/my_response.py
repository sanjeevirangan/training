import json


class MyResponse(object):
    def __init__(self):
        self.headers = {"Content-Type": "application/json"
                        }
        self.header_text = ""
        self.body = []
        self.status_code = 200
        self.body_json = " "
        self.__content_length = 0
        self.status_message = {200: 'OK',
                               400: 'Bad Request',
                               500: 'Internal Server Error',
                               501: 'Not Implemented',
                               503: 'Service Unavailable'}

    def write(self):
        self.body_json = json.dumps(self.body)
        print "Status: {0} {1}".format(str(self.status_code), self.status_message[self.status_code])
        for key in self.headers.keys():
            if key.lower() != 'content-type':
                print(key + ": " + self.headers[key])
        print "Content-Length: {0}".format(len(self.body_json))
        print "Content-Type: {0}".format(self.headers['Content-Type'])
        print  # End of headers
        print self.body_json