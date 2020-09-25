FROM openjdk:8u212-jre-alpine

WORKDIR /opt/cfg
COPY kafka/ ./kafka
COPY scripts ./
COPY config/server.properties ./kafka/config/
COPY ssl /var/private/ssl/

ENV KAFKA_HOME=/opt/cfg/kafka

ENV PATH=${PATH}:${KAFKA_HOME}/bin

RUN chmod -R +x *.sh
RUN apk add --no-cache bash curl jq docker
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk
RUN apk add --no-cache --allow-untrusted glibc-2.29-r0.apk
RUN rm glibc-2.29-r0.apk

ENTRYPOINT ["sh", "./start_kafka.sh"]
