from model.model import Model

mdl=Model()
grafo=mdl.buildGraph(1867)
print(f"Il grafo ha {mdl.get_num_nodes()} nodi e {mdl.get_num_edges()} archi")
for i in mdl._nodes:
    print(mdl.ottieni_grado(i))