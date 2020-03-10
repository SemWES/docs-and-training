#!/bin/bash

docker stop kafka_sh
docker build -t dfki/kafka_sh ./
docker network create semwes_kafka
docker run -it --rm --entrypoint=/bin/bash --name=kafka_sh --network semwes_kafka dfki/kafka_sh
