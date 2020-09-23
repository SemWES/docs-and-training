#!/bin/bash

docker stop kafka_sh
docker build -t dfki/kafka_sh ./

#docker run -it --rm --entrypoint=/bin/bash --name=kafka_sh --network kafka_net dfki/kafka_sh
docker run -it --rm --entrypoint=/bin/bash --name=kafka_sh --network host dfki/kafka_sh
