# SemWES Stream Data Integration

Due to its flexible webservice-based workflow structure, SemWES does natively support the integration of streaming data into SemWES workflow.

To develop SemWES workflows that handle streaming data one has to:
* maintain a server to host streaming data
* create producer and consumer SemWES services to provide and process the data
* integrate those services into SemWES as usual and create workflows using

## Apache Kafka Example
To demonstrate SemWES capabilities, a small ready-to-test protpotype is provided [in the code examples](../code_examples/ApacheKafka/prototype/README.md).
