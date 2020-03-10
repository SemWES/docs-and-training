#!/bin/sh

DATA=/opt/sema2flow/scripts/soap_requests/get_token.xml

RESPONSE=`curl -s --header "Content-Type: text/xml;charset=UTF-8" --header "SOAPAction: getSessionToken" --data @$DATA https://api.hetcomp.org:443/authManager/AuthManager`

echo $RESPONSE | sed -n "s/.*<return>\(.*\)<\/return>.*/\1/p"
