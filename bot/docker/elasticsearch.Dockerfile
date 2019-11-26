FROM docker.elastic.co/elasticsearch/elasticsearch:7.4.2

RUN mkdir backup

RUN chown -R elasticsearch:elasticsearch backup
