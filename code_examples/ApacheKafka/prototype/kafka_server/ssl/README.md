# TLS

To enable TSL, multiple steps need to be performed:
  1. generate SSL certificate for broker (optionally sign certificate), and register in broker's keystore
  2. generate SSL certificates for all Kafka clients/services (optionally sign certificates)
  3. register client certificates in broker's truststore
  4. register broker certificate in clients' truststores or directly with clients (depends on client implementation)
  5. configure broker to employ TLS
  6. configure clients to employ TLS

Further details can be found in the official Kafka documentation (https://kafka.apache.org/documentation/#security_ssl).

## Configure Broker to employ TLS

Most of the broker configuration to employ TLS/SSL has been prepared to ease the set-up of the server:
  - The directory `ssl` needs to hold the broker's keystore and truststore. Details on certificate generation and integration can be found in the official Kafka documentation (https://kafka.apache.org/documentation/#security_ssl).
  - The `.env` file needs to be adapted to provide the correct filenames and passwords:
    - `TRUSTSTORENAME`, filename of the broker's truststore, e.g. `kafka.broker0.truststore.jks`
    - `TRUSTSTOREPW`, password for the broker's truststore
    - `KEYSTORENAME`, filename of the broker's keystore, e.g. `kafka.broker0.keystore.jks`
    - `KEYSTOREPW`, password for the broker's keystore
    - `KEYPW`, password of the broker's certificate key
