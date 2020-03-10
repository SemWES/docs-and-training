
# Apache Kafka Stream Data Integration Prototype

This prototype demonstrates SemWES' capabilities to integrate data streams using the popular distributed streaming platform [Apache Kafka](https://kafka.apache.org/) .

The examplary setup consists of 3 components: 
 - [Kafka Server/Broker](kafka_server/README.md), stores all stream data and provides interfaces to access them
 - [Kafka Services](kafka_services/README.md), simple producer and consumer web services to interact with the data streams
 - [Kafka sh](kafka_sh/README.md), a shell instance to manually test all components

All components are deployed using docker and are connected to the same docker network "semwes_kafka", to easily and securely communicate with each other.

To ease the setup, a set of ssh keys and passwords has already been created, details can be found in a [dedicated README](ssl/README.md). If you use this prototype in production, please regenerate all keys and register them with the respective components, as shown in the previously mentioned ReadMe.

Note: Users running docker on Windows/Mac have to remark that the docker instance is hosted in a local VM. In this setup the exposed ports of containers cannot be forwarded to the host-machine, but are accessible throught the VM's IP.

## kafka_server

This directory contains the resources to set up a kafka server/broker encapsulated in a docker container.
By default the Kafka broker is available trough 3 different ports:
 - 9094, only via docker network, plain
 - 9093, only via docker network, ssl
 - 9092, external port, ssl
 
This behaviour can be changed by adapting [the server configuration](kafka_server/conf/server.properties), as well as [the docker compose configuration](kafka_server/docker-compose.yml).

## kafka_services

The directory kafka_service encapsulates the sources to build a docker container including a tomcat instance to host webservices.
In this prototype two services are integrated: a simple kafka producer, and a simple kafka consumer webservice.
Both webservices are made availabe to the host-machine at port 8282.


### Producer service

The producer's wsdl is hosted at:
	``http://<IP_of_Docker_host>:8282/kafkaproducerservice/ProducerService?wsdl``
 
 
### Consumer service

The consumer's wsdl is hosted at: 
 ``http://<IP_of_Docker_host>:8282/kafkaconsumerservice/ConsumerService?wsdl``
 
## Security

### Secure connection (TLS) between Kafka Server and Producer and Consumer Services
To enable TLS between the Kafka server and the clients, SSL keys have to be generated and registered manually on both sides. In the in-depth README's for the [Kafka server](kafka_server/README.md) and the [Kafka Services](kafka_services/README.md)  detailed instructions on this topic can be found.

Apache Kafka's documentation on encryption and authentication via SSL can be found here:
https://kafka.apache.org/documentation/#security_ssl

### Access control
If multiple streams are hosted on the same Kafka server and multiple partners’ services shall have access to only a subset of them, granular rules to access those streams must be put in place. Apache Kafka implements the concept of access control lists (ACLs) and thereby allows the maintainers of Kafka servers to manage the access to streams and the available actions (read/write) on those streams. More on this topic can be found in the official documentation: https://kafka.apache.org/documentation/#security_authz