FROM centos:7 as centos

FROM tinkerpop/gremlin-server:latest as gremlin

COPY --from=centos /* /

ENV GREMLIN_YAML /opt/gremlin-server/conf/gremlin-server-neo4j.yaml

COPY ./gremlin-server.yaml /opt/gremlin-server/conf/gremlin-server.yaml

COPY ./gremlin-server-classic.yaml /opt/gremlin-server/conf/gremlin-server-classic.yaml

COPY ./neo4j-empty.properties /opt/gremlin-server/conf/neo4j-empty.properties

RUN /opt/gremlin-server/bin/gremlin-server.sh install org.apache.tinkerpop neo4j-gremlin 3.4.7

RUN /opt/gremlin-server/bin/gremlin-server.sh install com.steelbridgelabs.oss neo4j-gremlin-bolt 0.4.2

CMD ["conf/gremlin-server-neo4j.yaml"]

# CMD ["conf/gremlin-server-classic.yaml"]