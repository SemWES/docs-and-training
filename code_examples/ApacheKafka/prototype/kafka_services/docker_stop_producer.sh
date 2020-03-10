#!/bin/sh

if [ "$#" -lt 1 ]; then
    echo "Usage: stop_producer.sh <serviceID>"
	exit
fi

docker exec kafkaservices ./stop_producer.sh $1
