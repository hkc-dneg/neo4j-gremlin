### Neo4J with Gremlin

A sample configuration of getting Neo4j working with tinkerpop.

	cd dist
	docker-compose build . -t neo4j-gremlin ; docker-compose-up


The python script relies on the example Movie graph being present. It can be created from the Neo4j browser or using the cypher query found in `dist/neo4j/custom`
