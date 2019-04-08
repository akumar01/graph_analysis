import networkx as nx
import numpy as nmp

# Controllability Grammian for adjacency matrix A
# over time horizon T, assuming that any node
# can be controlled
def controllability_matrix(A, T):
	p = A.shape[0]
	C = np.concatenate([np.power(A, t) for T in np.arange(T)])
	return C

def controllability_grammian(A, T):
	C = controllability_matrix(A, T)
	return C @ C.T