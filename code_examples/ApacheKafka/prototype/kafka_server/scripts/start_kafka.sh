#!/bin/sh
sleep 5s
./set_configs.sh
exec ./kafka/bin/kafka-server-start.sh ./kafka/config/server.properties