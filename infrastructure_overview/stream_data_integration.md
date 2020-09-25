# SemWES Stream Data Integration

Due to its flexible webservice-based workflow structure, SemWES does natively support the integration of streaming data into SemWES workflow.

To develop SemWES workflows that handle streaming data one has to:
* maintain a server to host streaming data
* create producer and consumer SemWES services to provide and process the data
* integrate those services into SemWES as usual and create workflows using them

## Apache Kafka Example
To demonstrate SemWES capabilities, a small ready-to-test prototype is provided [in the code examples](../code_examples/ApacheKafka/prototype/README.md).

### Demo services and workflow

Demo versions of these service are hosted at:
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
