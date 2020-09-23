# Apache Kafka Stream Data Integration Prototype

This prototype demonstrates SemWES' capabilities to integrate data streams using the popular distributed streaming platform [Apache Kafka](https://kafka.apache.org/) .

The exemplary setup consists of 3 components:
  - [Kafka Server/Broker](#kafka_server), stores all stream data and provides interfaces to access them
  - [Kafka Services](#kafka_services), simple producer and consumer web services to interact with the data streams
  - [Kafka sh](kafka_sh), a shell instance to manually test all components

All components are deployed using [docker](https://www.docker.com/).
To build, run, and test these, you only need to have Docker installed. All further software dependencies are bundled in the Docker containers.

**This prototype does not employ TLS/SSL** to secure the connections between the different components. However, for production environments it is highly advised to enable TLS/SSL to secure your data. Details can be found [below](#security), as well as in the dedicated component README's.

## kafka_server

This directory contains the resources to set up a kafka server/broker encapsulated in a docker container.
By default the Kafka broker is available trough 4 different ports:
  - 9092, only via docker network, ssl
  - 9093, only via docker network, plain
  - 9094, external port, ssl
  - 9095, external port, plain

Further details on how to configure the Kafka Server can be found in [the dedicated README](./kafka_server/README.md).

## kafka_services

The directory `kafka_services` encapsulates two python web services, a producer and a consumer.

### Producer Service
Further details on this service can be found in the [dedicated README](./kafka_services/python/kafka_producer/README.md).

### Consumer Service
Further details on this service can be found in the [dedicated README](./kafka_services/python/kafka_consumer/README.md).

### Client deployment in SemWES

To deploy you Kafka clients within SemWES the easiest way is to use the automated deployment, see the [service-deployment manual](https://github.com/SemWES/docs-and-training/blob/master/service_implementation/deployment_automated.md) or the [Service creation and deployment tutorial](https://github.com/SemWES/docs-and-training/blob/master/tutorials/workflows/basics_service_deployment.md).

#### Demo services and workflow

Demo versions of these service are hosted at and were deployed using the automated deployment mechanism:
```
https://srv.hetcomp.org/demo-kafka-consumer/KafkaConsumerService?wsdl
https://srv.hetcomp.org/demo-kafka-producer/KafkaProducerService?wsdl
```
They are registered at SemWES with the following service URIs:

```
http://dfki/sync/startProducer.owl#startProducer_Service
http://dfki/async/startConsumer.owl#startConsumer_Service
```

For demonstration purposes they have been integrated in the following workflow hosted at SemWES (requires a running Kafka server to test):
```
http://demo/workflow/Demo_KafkaChain.owl#Demo_KafkaChain
```

## kafka_sh

This directory encapsulates a docker container giving access to simple sh to manually interact with Kafka Streams.

Further details can be found in [the dedicated README](./kafka_sh/README.md).

## Security

### Secure connection (TLS) between Kafka Server and Producer and Consumer Services
**This prototype does not employ TLS** to secure the connection between the kafka broker and clients, but to ensure the security of the data TLS has to be set up correctly.
To enable TLS between the Kafka server and the clients, SSL keys have to be generated and registered manually on both sides. The README for the [Kafka server](kafka_server/README.md) offers further instructions on how to integrate TLS.

Additionally, Apache Kafka's documentation on encryption and authentication via SSL can be found here:
https://kafka.apache.org/documentation/#security_ssl

### Access control
If multiple streams are hosted on the same Kafka server and multiple partners’ services shall have access to only a subset of them, granular rules to access those streams must be put in place. Apache Kafka implements the concept of access control lists (ACLs) and thereby allows the maintainers of Kafka servers to manage the access to streams and the available actions (read/write) on those streams. More on this topic can be found in the official documentation: https://kafka.apache.org/documentation/#security_authz
