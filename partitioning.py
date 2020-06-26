#!/usr/bin/env python3
#
# usage: python3 partitioning.py list.txt

import numpy as np
import sys

nodes = []
edges = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        i, j = map(int, line.split())
        nodes.append(i)
        nodes.append(j)
        edges[(i, j)] = 1

nodes = list(set(nodes))

n = len(nodes)
A = np.zeros((n, n))

for i in nodes:
    for j in nodes:
        if (i, j) in edges.keys():
            A[i - 1, j - 1] = edges[(i, j)]

D = np.diag(np.sum(A, axis=1))
L = D - A

eigenval, eigenvec = np.linalg.eigh(L)

eigenvec = eigenvec.T

for i in range(len(eigenvec)):
    eigenvec[i] = eigenvec[i] / np.linalg.norm(eigenvec[i])

# l = eigenval[1]
# print(l / n)
x = list(eigenvec[1])
# print(x)

threshold = 0
s = []
for i, val in enumerate(x):
    if val > threshold:
        s.append(i + 1)

s_hat = list(set(nodes) - set(s))

es = []
for i in s:
    for j in s_hat:
        if (i, j) in edges.keys():
            es.append((i, j))

cut_ratio = len(es) / (len(s) * len(s_hat))

print(cut_ratio)
print(' '.join(map(str, s)))
