import networkx as nx
import qstest as qs

def test1():
	network = nx.karate_club_graph()
	communities = qs.louvain_algorithm(network)
	sg, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain_algorithm)
	assert len(sg)==len(communities)
	assert len(pvals)==len(communities)
	assert max(pvals)<=1.0
	assert min(pvals)>=0.0

def test2():
	network = nx.karate_club_graph()
	communities = qs.louvain_algorithm(network)
	sg, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain_algorithm, num_of_thread = 1)
	assert len(sg)==len(communities)
	assert len(pvals)==len(communities)
	assert max(pvals)<=1.0
	assert min(pvals)>=0.0
