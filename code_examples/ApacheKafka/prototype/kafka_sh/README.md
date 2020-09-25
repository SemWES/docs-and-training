
# INFO

This Docker container can be used to manually test the kafka setup.
It will run a shell in a docker container that contains the necessary resources to create kafka command-line producers and consumers, as well as to create and list kafka-topics.

To get started, one has to download the latest version of Apache Kafka (https://kafka.apache.org/downloads), extract it and move the content to the `./kafka/` directory.

## TLS

To enable the shell client to establish a secure connection to a broker, please follow the official README [availale here](https://kafka.apache.org/documentation/#security_configclients). Basically, a configuration file has to be created and used when executing the producer or consumer scripts.

# HowTo

## (re)build and (re)start docker container, opens shell in terminal
```
./rebuild_and_restart.sh
```

## exit shell
```
exit
```

## to connect an additional shell to the already running docker instance
```
./connect_additional_shell.sh
```

## interaction with kafka
All parts in `<>` have to be replaces with the correct values.

### create a topic
```
bin/kafka-topics.sh --create --bootstrap-server <kafka_broker_IP>:<broker_port> --replication-factor 1 --partitions 1 --topic <topicname>
```

### list all topics
```
bin/kafka-topics.sh --list --bootstrap-server <kafka_broker_IP>:<broker_port>
```

### send some messages
```
bin/kafka-console-producer.sh --broker-list <kafka_broker_IP>:<broker_port> --topic <topic>
```

### retrieve messages
```
bin/kafka-console-consumer.sh --bootstrap-server <kafka_broker_IP>:<broker_port> --topic <topic> --from-beginning
```
