FROM openjdk:8u212-jre-alpine

WORKDIR /opt/sema2flow
COPY kafka/ ./kafka

ENV KAFKA_HOME=/opt/sema2flow/kafka

ENV PATH=${PATH}:${KAFKA_HOME}/bin

RUN chmod -R +x kafka/bin/*.sh
RUN apk add --no-cache bash curl jq docker
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk
RUN apk add --no-cache --allow-untrusted glibc-2.29-r0.apk
RUN rm glibc-2.29-r0.apk

WORKDIR /opt/sema2flow/kafka