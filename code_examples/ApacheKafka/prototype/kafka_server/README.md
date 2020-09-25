# Kafka Server Info

This directory encapsulates multiple docker containers that are required to set up a kafka server: a zookeeper server and a kafka broker. The broker can be seen as the interface to the underlying data.

docker-compose is used to easily build, connect, maintain those docker instances.

To get started, download the latest version of Apache Kafka (https://kafka.apache.org/downloads), extract it and move the content to the `./kafka/` directory. Then you should, for example, have the following structure: `./kafka/bin/kafka-server-start.sh`.

# Configuration

## Host IP
 - adapt the `.env` file to set the external IP and port of the host environment to automatically configure the correct IP for Kafka's external ports, `HOSTIP` and `EXTPORT`
 - adapt the `.env` to configure TLS, for more details see [below](#TLS)

## Open Ports
 - defined in conf/server.properties lines 31 - 47
 - pre-configured:
   - 9092, only via docker network, ssl
   - 9093, only via docker network, plain
   - 9094, external port, ssl
   - 9095, external port, plain

## TLS

To enable TSL, multiple steps need to be performed:
  1. generate SSL certificate for broker (optionally sign certificate), and register in broker's keystore
  2. generate SSL certificates for all Kafka clients/services (optionally sign certificates)
  3. register client certificates in broker's truststore
  4. register broker certificate in clients' truststores or directly with clients (depends on client implementation)
  5. configure broker to employ TLS
  6. configure clients to employ TLS

Further details can be found in the official Kafka documentation (https://kafka.apache.org/documentation/#security_ssl).

### Configure Broker to employ TLS

Most of the broker configuration to employ TLS/SSL has been prepared to ease the set-up of the server:
  - The directory `ssl` needs to hold the broker's keystore and truststore. Details on certificate generation and integration can be found in the official Kafka documentation (https://kafka.apache.org/documentation/#security_ssl).
  - The `.env` file needs to be adapted to provide the correct filenames and passwords:
    - `TRUSTSTORENAME`, filename of the broker's truststore, e.g. `kafka.broker0.truststore.jks`
    - `TRUSTSTOREPW`, password for the broker's truststore
    - `KEYSTORENAME`, filename of the broker's keystore, e.g. `kafka.broker0.keystore.jks`
    - `KEYSTOREPW`, password for the broker's keystore
    - `KEYPW`, password of the broker's certificate key

## Docker Network

To ease local testing, the kafka containers are using the docker network `kafka_net_cfg`. Other containers hosted on the same machine can be added to this network to easily connect to the kafka broker, e.g. using the container name as the domain name `kafka_broker:9093`.

To change this behaviour, the `docker-compose.yml`, lines 15 - 18 have to be adapted.

# HowTo

## (re)build and (re)start docker containers

`./rebuild_and_restart.sh`

## check logs

`docker-compose logs -f`

`docker logs -f kafka_broker`

`docker logs -f zookeeper`

Press `CTRL + c` to stop inspecting logs.

## stop

`./stop`
