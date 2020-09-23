#!/usr/bin/env python
import sys
import datetime
import time
from kafka import KafkaConsumer

# command = ['python', 'consume_data.py', statusfile, resultfile, logfile, serviceID, brokerIP, brokerPort, topic, timeout]

def main():
    statusfile = sys.argv[1]
    resultfile = sys.argv[2]
    logfile = sys.argv[3]
    serviceID = sys.argv[4]
    brokerIP = sys.argv[5]
    brokerPort = sys.argv[6]
    topic = sys.argv[7]
    timeout = int(sys.argv[8])

    consumer = KafkaConsumer(topic, auto_offset_reset='earliest', bootstrap_servers=f'{brokerIP}:{brokerPort}', group_id=serviceID, consumer_timeout_ms=200)
    with open(resultfile, 'w') as f:
        f.write('UNSET')

    for current_time in range(timeout):
        status = "%d" % round(100*(current_time+1)/timeout)
        # print(f"Updating status to: {status} - current time = {current_time}; timeout = {timeout}", flush=True)
        with open(statusfile, 'w') as f:
            f.write(str(status))
            f.flush()
		
        with open(logfile, 'a') as f:
            for msg in consumer:
                log = f"{datetime.datetime.now().strftime('%y_%m_%d-%H_%M_%S')} : {msg.value.decode()}\n"
                f.write(log)
                f.flush()

        if current_time == timeout - 1:
            with open(resultfile, 'w') as f:
                f.write('FINISHED')
        time.sleep(1)


if __name__ == "__main__":
    main()
