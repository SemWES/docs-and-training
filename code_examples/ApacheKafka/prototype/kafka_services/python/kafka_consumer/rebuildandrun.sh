#!/bin/bash

# Builds and runs the container locally (for testing purposes)

# changing cname will require to adapt the test_client (test.py, line 54) accordingly
cname=kafka_consumer

if [ -z "$1" ]
  then
    echo No port given, setting port to 821
    port=821
else
  port=$1
fi

docker kill $cname
docker rm $cname
docker build -t $cname .

# depending on the specific setup different network configurations might be required:
#docker run -d -p $port:80 --env-file=env --network host --name $cname $cname
#docker run -d -p $port:80 --env-file=env --network kafka_net_cfg --name $cname $cname
docker run -d -p $port:80 --env-file=env --name $cname $cname
