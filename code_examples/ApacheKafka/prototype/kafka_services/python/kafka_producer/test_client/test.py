#!/usr/bin/env python
"""Simple test client to call the KafkaProducerService, requires python 3.6"""

import os
import sys
import time
import random

from suds.client import Client
from suds.cache import NoCache
from suds import WebFault, MethodNotFound


def soap_call(wsdl_url, methodname, method_args):
    """Calls a SOAP webmethod at a given URL with given arguments."""
    client = Client(wsdl_url, cache=NoCache())

    try:
        method = getattr(client.service, methodname)
    except MethodNotFound as error:
        return error

    try:
        response = method(*method_args)
    except WebFault as error:
        return error

    return response


def main():
    """Makes a series of test calls and prints their outputs."""

    try:
        host_address_service = int(sys.argv[1])
        print(f"Using host address {host_address_service}")
    except:
        host_address_service = "localhost"
        print("Couldn't get host address of the producer service from commandline argument, using localhost.")

    try:
        port_service = int(sys.argv[2])
        print(f"Using port {port_service}")
    except:
        port_service = 820
        print(f"Couldn't get port of the producer service from commandline argument, using {port_service}.")

    try:
        serviceid = int(sys.argv[3])
        print(f"Using serviceid {serviceid}")
    except:
        serviceid = "testid_" + str(int(time.time())) + "-" + str(random.randint(0, 10000))
        print(f"Couldn't get serviceid from commandline argument, using {serviceid}.")

    try:
        host_address = int(sys.argv[4])
        print(f"Using host address {host_address}")
    except:
        host_address = "92.78.102.187"
        print(f"Couldn't get kafka broker host address from commandline argument, using default: {host_address}")

    try:
        port = int(sys.argv[5])
        print(f"Using port {port}")
    except:
        port = 59092
        print(f"Couldn't get port from commandline argument, using default: {port}.")

    try:
        timeout = int(sys.argv[6])
        print(f"Using timeout {timeout}")
    except:
        timeout = 5
        print(f"Couldn't get timeout from commandline argument, using {timeout}s.")

    try:
        topic = int(sys.argv[7])
        print(f"Using topic {topic}")
    except:
        topic = "testtopic_" + str(random.randint(0, 10000))
        print(f"Couldn't get topic from commandline argument, using {topic}.")

    try:
        context_root = os.environ["CONTEXT_ROOT"]
    except KeyError:
        context_root = '/demo-kafka-producer'
        print(f"Error: environment variable CONTEXT_ROOT not set, using default: {context_root}.")



    # URL of the SOAP service to test. Modify this if the deployment location changes.
    # Docker containers can be addressed via their container name
    url = f"http://{host_address_service}:{port_service}{context_root}/KafkaProducerService?wsdl"
    print(f"Service URL is {url}")

    print("Testing start of producer:")
    response = soap_call(url, "startProducer", [id, host_address, port, topic, int(timeout + 5)])
    print(f"Start result = {response}")

    print(f"Waiting {timeout} seconds until producer is stopped")
    time.sleep(timeout)

    response2 = soap_call(url, "abortProducer", [id])
    print(f"Producer stop successful: {response2}")

    print(f"Test finished")


if __name__ == "__main__":
    main()
