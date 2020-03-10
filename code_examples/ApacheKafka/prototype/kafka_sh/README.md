
# Kafka shell client

This Docker container can be used to manually test the kafka setup.
It will run a shell in a docker container that contains the necessary resources to create kafka command-line producers and consumers, as well as to create and list kafka-topics.

To get started, one has to download the latest version of Apache Kafka (https://kafka.apache.org/downloads), extract it and move the content to the `./kafka/` directory.

This container uses port 9094 of the kafka-server sending plain messages (no TLS), as it is only available to containers hosted in the same docker network.


# HowTo


## (re)build and (re)start docker container, opens shell in terminal

``./rebuild_and_restart.sh``

## exit shell

``exit``
 
## to connect an additional shell to the already running docker instance

``./connect_additional_shell.sh``

## interaction with kafka

### create a topic

``bin/kafka-topics.sh --create --bootstrap-server kafka_broker:9094 --replication-factor 1 --partitions 1 --topic test``

### list all topics 

``bin/kafka-topics.sh --list --bootstrap-server kafka_broker:9094``

### send some messages

``bin/kafka-console-producer.sh --broker-list kafka_broker:9094 --topic test``

### retrieve messages

``bin/kafka-console-consumer.sh --bootstrap-server kafka_broker:9094 --topic test --from-beginning``