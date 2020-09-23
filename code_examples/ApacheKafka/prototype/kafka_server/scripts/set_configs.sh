#!/bin/sh
CONF=/opt/cfg/kafka/config/server.properties

sed -i "s/<HOSTIP>/${HOSTIP}/g" $CONF
sed -i "s/<EXTPORT>/${EXTPORT}/g" $CONF
sed -i "s/<TRUSTSTORENAME>/${TRUSTSTORENAME}/g" $CONF
sed -i "s/<TRUSTSTOREPW>/${TRUSTSTOREPW}/g" $CONF
sed -i "s/<KEYSTORENAME>/${KEYSTORENAME}/g" $CONF
sed -i "s/<KEYSTOREPW>/${KEYSTOREPW}/g" $CONF
sed -i "s/<KEYPW>/${KEYPW}/g" $CONF
