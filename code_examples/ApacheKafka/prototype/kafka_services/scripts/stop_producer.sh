#!/bin/sh

if [ "$#" -lt 1 ]; then
    echo "Usage: stop_producer.sh <serviceID>"
	exit
fi

DATA=/opt/sema2flow/scripts/soap_requests/stop_prod.xml


TOKEN=`./get_token.sh`

sed -i "s/<sessionToken>.*<\/sessionToken>/<sessionToken>$TOKEN<\/sessionToken>/g" "$DATA"
sed -i "s/<serviceID>.*<\/serviceID>/<serviceID>$1<\/serviceID>/g" "$DATA"

RESPONSE=`curl -s --header "Content-Type: text/xml;charset=UTF-8" --header "SOAPAction: stopProducer" --data @$DATA localhost:8080/kafkaproducerservice/ProducerService`

echo $RESPONSE | sed -n "s/.*<response>\(.*\)<\/response>.*/\1/p"
