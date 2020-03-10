#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: start_producer.sh <serviceID> <kafkaTopic>"
	exit
fi

DATA=/opt/sema2flow/scripts/soap_requests/start_prod.xml


TOKEN=`./get_token.sh`

sed -i "s/<sessionToken>.*<\/sessionToken>/<sessionToken>$TOKEN<\/sessionToken>/g" "$DATA"
sed -i "s/<serviceID>.*<\/serviceID>/<serviceID>$1<\/serviceID>/g" "$DATA"
sed -i "s/<topic>.*<\/topic>/<topic>$2<\/topic>/g" "$DATA"

RESPONSE=`curl -s --header "Content-Type: text/xml;charset=UTF-8" --header "SOAPAction: startProducer" --data @$DATA localhost:8080/kafkaproducerservice/ProducerService`

echo $RESPONSE | sed -n "s/.*<response>\(.*\)<\/response>.*/\1/p"
