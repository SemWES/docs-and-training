#!/bin/sh

if [ "$#" -lt 1 ]; then
    echo "Usage: stop_consumer.sh <serviceID>"
	exit
fi

docker exec kafkaservices ./stop_consumer.sh $1
