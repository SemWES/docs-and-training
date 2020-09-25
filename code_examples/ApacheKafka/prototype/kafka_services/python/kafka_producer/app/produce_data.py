#!/usr/bin/env python
import sys

from time import sleep
from kafka import KafkaProducer

# command = ['python', 'produce_data.py', serviceID, brokerIP, brokerPort, topic]

def main():
    producer_id = str(sys.argv[1])
    brokerIP = str(sys.argv[2])
    brokerPort = str(sys.argv[3])
    topic = str(sys.argv[4])
    timeout = int(sys.argv[5])
    producer = KafkaProducer(bootstrap_servers=f'{brokerIP}:{brokerPort}')

    print(f"Producer {producer_id} - writing to topic: {topic}", flush=True)

    counter = 1
    # Simply send a set of messages to the topic
    for current_time in range(timeout):
        message = f'Producer {producer_id} - message number {counter}'
        # print(message)
        counter += 1
        future = producer.send(topic, message.encode())
        if not future.get(timeout=30):
            print(f"!! Message ({counter}) not sent successfully.", flush=True)
        sleep(1)

if __name__ == "__main__":
    main()
