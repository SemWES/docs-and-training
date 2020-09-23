# TLS

To enable TSL, multiple steps need to be performed:
  1. generate SSL certificate for broker (optionally sign certificate), and register in broker's keystore
  2. generate SSL certificates for all Kafka clients/services (optionally sign certificates)
  3. register client certificates in broker's truststore
  4. register broker certificate in clients' truststores or directly with clients (depends on client implementation)
  5. configure broker to employ TLS
  6. configure clients to employ TLS

Further details can be found in the official Kafka documentation (https://kafka.apache.org/documentation/#security_ssl).

## Configure shell client to employ TLS

To enable the shell client to establish a secure connection to a broker, please follow the official README [availale here](https://kafka.apache.org/documentation/#security_configclients). Basically, a configuration file has to be created and used when executing the producer or consumer scripts.
