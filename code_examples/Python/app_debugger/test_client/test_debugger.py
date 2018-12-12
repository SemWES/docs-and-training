#!/usr/bin/env python
"""Simple test client to call the debugger SOAP service"""

import os
import sys
import base64

from suds.client import Client
from suds.cache import NoCache
from suds import WebFault, MethodNotFound


def soap_call(wsdl_url, methodname, method_args):
    """Calls a SOAP webmethod at a given URL with given arguments."""
    client = Client(wsdl_url, cache=NoCache())

    try:
        method = getattr(client.service, methodname)
    except MethodNotFound as error:
        return(error)

    try:
        response = method(*method_args)
    except WebFault as error:
        return(error)

    return response


def main():
    try:
        port = int(sys.argv[1])
        print("Using port {}".format(port))
    except:
        print("Couldn't get port from commandline argument, using 80.")
        port = 80

    try:
        context_root = os.environ["CONTEXT_ROOT"]
    except KeyError:
        print("Error: environment variable CONTEXT_ROOT not set.")
        exit(1)

    url = "http://localhost:{}{}/Debugger?wsdl".format(port, context_root)
    print("wsdl URL is {}".format(url))

    print("Calling displayParameters()")
    response = soap_call(url, "displayParameters", ["serviceID1", "sessionToken", "WFM=https://blablabla.com/WFM?wsdl,", "Some input", "Label1", "Second input", "Label2"])
    html = base64.b64decode(response).decode()
    with open("test.html", 'w') as fout:
        fout.write(html)
    print("Result written to test.html")


if __name__ == "__main__":
    main()
