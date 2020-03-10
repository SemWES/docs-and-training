#!/bin/sh
CONF=/opt/sema2flow/conf/authenticator-client.properties
TOKEN_REQ=/opt/sema2flow/scripts/soap_requests/get_token.xml

sed -i "s/<AUTH_USER>/${AUTH_USER}/g" $CONF
sed -i "s/<AUTH_PW>/${AUTH_PW}/g" $CONF
sed -i "s/<AUTH_PROJECT>/${AUTH_PROJECT}/g" $CONF


sed -i "s/AUTH_USER/${AUTH_USER}/g" $TOKEN_REQ
sed -i "s/AUTH_PW/${AUTH_PW}/g" $TOKEN_REQ
sed -i "s/AUTH_PROJECT/${AUTH_PROJECT}/g" $TOKEN_REQ

echo "Configurations have been set"