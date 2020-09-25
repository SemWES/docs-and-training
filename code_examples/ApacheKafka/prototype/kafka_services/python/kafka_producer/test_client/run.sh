#! /bin/bash

docker run --network s2f_kafka --env-file=../env -w /usr/src/test_client testclient python test.py $1 $2
