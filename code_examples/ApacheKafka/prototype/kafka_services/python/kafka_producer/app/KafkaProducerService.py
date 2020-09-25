"""A very simple calculator SOAP service written in Python.

This simple service utilizes the "flask_spyne" package to create a SOAP service
with just a few lines of code.
"""
import logging
import subprocess
import os
import signal

from spyne import Application, srpc, ServiceBase, Unicode, Boolean, Integer
from spyne.protocol.soap import Soap11

# Define the target namespace
TNS = "kafka_producer.dfki.de"
# Define the name under which the service will be deployed
SERVICENAME = "KafkaProducerService"
PID_FILE = "pid.txt"

TMPDIR = os.environ["LOG_FOLDER"]


class KafkaProducerService(ServiceBase):
    """The actual spyne service

    Note that the class name is _not_ important for the endpoint URL of the
    service (that's defined by __service_url_path__), but it will show up in
    the service WSDL as the service name.
    """
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Boolean)
    def startProducer(serviceID, brokerIP, brokerPort, topic, timeout):

        # The SemWES engine generates serviceID which look as follows: <workflowID>_<stepnumber>
        # with workflowID being the unique execution ID of the running workflow.
        # and stepnumber a unique identifier for the current service within the workflow
        # to identify the current execution, we only need the workflow identifier
        serviceID = serviceID.split("_")[0]

        try:
            logging.info(f"Starting producer {serviceID} process, with topic {topic}")
            command = ['python', 'produce_data.py', serviceID, brokerIP, brokerPort, topic, timeout]
            process = subprocess.Popen(command)

            if not os.path.exists(TMPDIR):
                os.mkdir(TMPDIR)

            with open(os.path.join(TMPDIR, PID_FILE), 'w') as f:
                f.write(f"{serviceID}={process.pid}")

        except Exception as ex:
            logging.error('Exception while publishing messages')
            logging.error(str(ex))
            return False
        return True

    @srpc(Unicode, _returns=Boolean)
    def abortProducer(serviceID):
        """Aborts a producer
        """

        # The SemWES engine generates serviceID which look as follows: <workflowID>_<stepnumber>
        # with workflowID being the unique execution ID of the running workflow.
        # and stepnumber a unique identifier for the current service within the workflow
        # to identify the current execution, we only need the workflow identifier
        serviceID = serviceID.split("_")[0]

        logging.info("abortProducer() called with producer id {}".format(serviceID))
        if not os.path.exists(TMPDIR):
            os.mkdir(TMPDIR)

        success = False
        with open(os.path.join(TMPDIR, PID_FILE), 'r') as f:
            lines = f.readlines()
        with open(os.path.join(TMPDIR, PID_FILE), 'w') as f:
            for line in lines:
                (current_producer_id, pid) = line.split("=")
                if serviceID == current_producer_id:
                    logging.info(f"aborting producer {serviceID} with pid {pid}")
                    try:
                        os.kill(int(pid), signal.SIGKILL)
                        success = True
                    except Exception as ex:
                        logging.error('Exception while aborting producer')
                        logging.error(str(ex))
                else:
                    f.write(line)
        return success

        return False

def create_app():
    """Creates an Application object containing the waiter service."""
    app = Application([KafkaProducerService], TNS,
                      in_protocol=Soap11(validator='soft'), out_protocol=Soap11())

    return app
