FROM tomcat:8.5
ENV JVM_PARAMS="-Xmx2g"

ENV WEBAPPS_CONFIGS /opt/sema2flow/conf/

COPY webapps/ /usr/local/tomcat/webapps/
COPY conf/ /opt/sema2flow/conf/
COPY ssl/ /var/private/ssl/
COPY tomcat_conf/ /usr/local/tomcat/conf/
COPY lib/ /usr/local/tomcat/lib/
COPY scripts/ /opt/sema2flow/scripts

WORKDIR /opt/sema2flow/scripts

EXPOSE 8080
ENTRYPOINT ["/bin/bash", "./start_tomcat.sh"]