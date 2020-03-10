#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: start_producer.sh <serviceID> <kafkaTopic>"
	exit
fi

docker exec kafkaservices ./start_producer.sh $1 $2
