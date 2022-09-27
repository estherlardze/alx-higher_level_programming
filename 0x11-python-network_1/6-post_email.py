#!/usr/bin/python3
'''
take a url and email, sends a post request to the url, with email as parameter
'''

import requests
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], email)
    print('{}'.format(response.text))
