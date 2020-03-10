#!/bin/bash

# docker-compose down will remove all external storages of the container instances
# only execute this if you truly would like to remove all data generated by kafka
# e.g. all streaming data, all consumer positions, etc
#docker-compose down

docker-compose stop
docker network create semwes_kafka
docker-compose up --build -d

