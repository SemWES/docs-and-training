#!/bin/bash

docker stop kafkaservices
docker rm kafkaservices
docker network create semwes_kafka
docker build -t dfki/kafkaservices ./
docker run -d -p 8282:8080 --env-file ./.env --name=kafkaservices --network semwes_kafka dfki/kafkaservices
