# Kafka Server

This directory encapsulates multiple docker containers that are required to set up a kafka server: a zookeeper server, and a kafka broker.
docker-compose is used to easily build, connect, maintain those docker instances.

To get started, one has to download the latest version of Apache Kafka (https://kafka.apache.org/downloads), extract it and move the content to the `./kafka/` directory.

This prototype is already pre-configured (ssl keys generated and integrated) so you can start testing right away.


# HowTo


## (re)build and (re)start docker containers 

``./rebuild_and_restart.sh``

## check logs

``docker-compose logs -f``

Press ``CTRL + c``   to stop inspecting logs.

## stop

``./stop``