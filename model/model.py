import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph=nx.Graph()
        self._nodes=[]
        self._codeMap={}


    def buildGraph(self, year):

        self._nodes=DAO.getAllNodes(year)
        for i in self._nodes:
            self._codeMap[i.CCode]=i
        self._graph.add_nodes_from(self._nodes)
        #print(len(self._graph.nodes))
        archi= DAO.getAllEdges(year)
        for i in archi:
            self._graph.add_edge(self._codeMap[i[0]], self._codeMap[i[1]])

    def get_num_compConnesse(self):
        return nx.number_connected_components(self._graph)

    def get_num_nodes(self):
        return len(self._graph.nodes)

    def get_num_edges(self):
        return len(self._graph.edges)

    def ottieni_grado(self, nodo):
        return f"{nodo} -- grado: {nx.degree(self._graph, nodo)}"

    def elementi_dd(self):
        for i in self._graph.nodes:
            print(type(i))
        return self._graph.nodes



    def connessa (self, source):
        if source is None:
            return None
        conn = nx.node_connected_component(self._graph, source)
        return conn

    def ottieni_nodo(self, code):
        return self._codeMap[int(code)]
