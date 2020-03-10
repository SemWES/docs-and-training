# Kafka Services

This directory encapsulates the resources to build docker containers hosting kafka clients. Multiple clients may be combined in one deployment to reduce resource consumption. In this case, it has to be ensured that the configuration files, as well as the .war files have unique names.

To configure the deployment of kafka clients correctly the following requirements have to be met:

 - __.env file:__
	In this file the login information for the authentication client (SemWES login) have to be entered. This is only required to enable local testing, once the services are integrated in SemWES and invoked through the SemWES WorkflowManager, sessiontokens will be provided automatically.:
	- AUTH_USER, SemWES username
	- AUTH_PW, SemWES password
	- AUTH_PROJECT, SemWES project


# HowTo


## (re)build and (re)start docker containers 

``./rebuild_and_restart.sh``

## check logs (continuously)

``docker logs -f kafkaservices``

Press ``CTRL + c``   to stop inspecting logs.

## check last 10 log entries

``docker logs kafkaservices --tail 10``

## stop

``./stop.sh``


# Sample execution

``./rebuild_and_restart``

``./docker_start_producer.sh 123 testTopic``

``./docker_start_consumer.sh 456 testTopic``

``docker logs kafkaservices --tail 100``

``./docker_stop_producer.sh 123``

``./docker_stop_consumer.sh 456``

``docker logs kafkaservices --tail 10``

``./stop.sh``


# Convenience scripts

## get SessionToken

``./docker_get_token.sh``

## start Producer

``./docker_start_producer.sh <serviceID> <kafkaTopic>``

## stop Producer

``./docker_stop_producer.sh <serviceID>``

## start Consumer

``./docker_start_consumer.sh <serviceID> <kafkaTopic>``

## stop Consumer

``./docker_stop_consumer.sh <serviceID>``