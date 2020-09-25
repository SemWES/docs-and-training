#!/bin/sh

# wait for zookeeper to finish starting
sleep 5s

# apply configurations (relace keywords from .env in server.properties)
./set_configs.sh
exec ./kafka/bin/kafka-server-start.sh ./kafka/config/server.properties
