from gremlin_python import statics
import gremlin_python
from gremlin_python.structure.graph import Graph
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __ as AnonymousTraversal
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier
from gremlin_python.process.traversal import Bindings
from gremlin_python.process.traversal import WithOptions


def main():
	g = traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin','g'))
	print("Count :", g.V().hasLabel('Movie').count().toList())
	print("Movies in the graph :", g.V().hasLabel('Movie').title.toList())


if __name__ == '__main__':
	main()