#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as \
            response:
        url = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(url)))
        print("\t- content: {}".format(url))
        print("\t- utf8 content: {}".format(url.decode('utf-8')))
