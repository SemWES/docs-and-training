# Simple Kafka Producer (Python)

The Simple Kafka Producer is a webservice which offers synchronous methods to connect to [Apache Kafka](https://kafka.apache.org/) streams and publish some static messages.

This service is mainly designed to showcase how to easily set up such a service and may be used as a template for more complex scenarios.

This service is based on the "synchronous calculator" template, whose documentation and sources can be found [here](https://github.com/SemWES/docs-and-training/blob/master/tutorials/services/python_sync_calculator.md).

## Demo

A demo version of this service is hosted at:
```
https://srv.hetcomp.org/demo-kafka-producer/KafkaProducerService?wsdl
```
It is registered at SemWES with the following service URI:

```
http://dfki/sync/startProducer.owl#startProducer_Service
```

For demonstration purposes it has been integrated in the following workflow hosted at SemWES (requires a running Kafka server to test):
```
http://demo/workflow/Demo_KafkaChain.owl#Demo_KafkaChain
```

## Methods
The service offers the following **synchronous** methods:
  - `startProducer(serviceID, brokerIP, brokerPort, topic, timeout)`: This method can be used to start a producer thread, automatically publishing some generic messages to the provided topic, hosted on the given broker. If not aborted, the thread will terminate itself after the `timeout` (seconds) has elapsed.
  - `abortProducer(serviceID)`: This method terminates a running producer thread, identified by its service id.

## Prerequisites
To build, and run this service, only [Docker](https://www.docker.com/) is required to be installed on the target machine. All further software dependencies are bundled in the Docker container.

For testing, a running Apache Kafka Server is required.

For further development based on this skeleton, it is highly recommended to use a local Python environment.

## Configure, build, and run the service

### Configuration

#### Project and Service Name
Per default the service's path is configured as:
```
https://<Host-IP>/demo-kafka_producer/KafkaProducerService
```

To change the service's path and prepare the service to be hosted in a different environment two files have to be adapted:
 - `env`, update line 2 (context root)
 - `app/main.py`, update line 17 (`build_interface_document`) to reflect the anticipated deployment path. This ensures that within the WSDL the address location is defined correctly.

##### SemWES deployment
To deploy this service on SemWES using the automated deployment approach ([manual](https://github.com/SemWES/docs-and-training/blob/master/service_implementation/deployment_automated.md), [tutorial](https://github.com/SemWES/docs-and-training/blob/master/tutorials/workflows/basics_service_deployment.md)) the context root has to be configured as follows:
```
CONTEXT_ROOT=/<project>-<service_name>
```
Here, `<project>` is the project name you use to log in to SemWES, and `<service_name>` is for you to choose. Please note that `<project>-<service_name>` must have a maximum length of 32 characters and must consist only of lowercase letters, digits, and hyphens.

#### Port
Per default the service uses port `820`. This can be configured in the `rebuildandrun.sh` file, line 12:
```
    # Default port
    port=820
```
Or, by running the `rebuildandrun.sh` script with an additional parameter and providing the port, see [Build and run](#build-and-run) below.

### Build and run
To compile the service source code, pack it into a Docker container, and run the container, run
```
./rebuildandrun.sh <port>
```

On the first run, this might take a while since the base container images need to be downloaded and dependencies need to be installed. Subsequent builds will complete significantly faster.

This run script starts the container in detached mode, meaning that the command returns immediately and that logs are not immediately visible.

#### check status

To check the status of your docker container run the following command, and look for the line where `IMAGE NAME` is `kafka_producer`:
```
docker ps
```

#### check logs (continuously)
```
docker logs -f kafka_producer
```
Press ``CTRL + c``   to stop inspecting logs.

#### check last 10 log entries
```
docker logs kafka_producer --tail 10
```

#### stop container
```
./stop.sh
```

### Testing the service
Once the container is running, it can be tested by using its published WSDL file to create a SOAP webclient and call methods with it.

The WSDL should per default be available at the following address, unless you have updated the context root or the main service file `app/KafkaProducerService.py`:
```
http://<IP_of_Docker_host>:820/demo-kafka-producer/KafkaProducerService?wsdl
```

To test the functionality of your service, you can either use some tooling, like [SoapUI](https://www.soapui.org/downloads/soapui/), a local client, or a commandline tool like cURL.

#### Local python client
This example includes a Python-based client application, found in the `test_client/` folder. If you have a local Python 3.x environment, you can simply run `python test_service.py` (make sure that all dependencies defined in `requirements.txt`) are installed. Alternatively, the example includes a Python Docker container for executing the test client.

To use the Python container, run
```
cd test_client
./build.sh      # run only once
./run.sh        # run every time you want to test
```

You can make changes to `test.py` to test other methods or other deployment locations. Rebuilding the container is not necessary after such changes.

## Use this example as a template
To use this example as a template for your own service development, simply copy the source code to another location and start editing. To understand the structure of the code, start with `main.py`, continue with `KafkaProducerService.py`, and then review `produce_data.py`.
