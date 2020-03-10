Perform the following steps to generate all keystores, certificates and truststores to secure the connection between the kafka broker and the clients. If you'd like to add more clients simply repeat steps 2, 3, 4, and 5 with different filenames and aliases.

Please use distinct passwords for the keystore, the respective key and the truststore for each entity.

1. Generate server keystore:
``keytool -keystore ./kafka.broker0.keystore.jks -genkey -keyalg RSA -alias kafkabroker0``

2. Generate client keystores:
``keytool -keystore ./kafka.consumer0.keystore.jks -genkey -keyalg RSA -alias kafkaconsumer0``
``keytool -keystore ./kafka.producer0.keystore.jks -genkey -keyalg RSA -alias kafkaproducer0``

3. Export certificate from keystores:
``keytool -export -alias kafkabroker0 -file kafkabroker0.cer -keystore kafka.broker0.keystore.jks``
``keytool -export -alias kafkaconsumer0 -file kafkaconsumer0.cer -keystore kafka.consumer0.keystore.jks``
``keytool -export -alias kafkaproducer0 -file kafkaproducer0.cer -keystore kafka.producer0.keystore.jks``

4. Create server truststore, import client certificates:
``keytool -import -file kafkaconsumer0.cer -alias kafkaconsumer0 -keystore kafka.broker0.truststore.jks``
``keytool -import -file kafkaproducer0.cer -alias kafkaproducer0 -keystore kafka.broker0.truststore.jks``

5. Create client truststores:
``keytool -import -file kafkabroker0.cer -alias kafkabroker0 -keystore kafka.consumer0.truststore.jks``
``keytool -import -file kafkabroker0.cer -alias kafkabroker0 -keystore kafka.producer0.truststore.jks``