#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: start_consumer.sh <serviceID> <kafkaTopic>"
	exit
fi

docker exec kafkaservices ./start_consumer.sh $1 $2
