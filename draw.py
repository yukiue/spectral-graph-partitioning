#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
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

x = list(eigenvec[1])
y = list(eigenvec[2])

threshold = 0
s = []
for i, val in enumerate(x):
    if val > threshold:
        s.append(i + 1)

s_hat = list(set(nodes) - set(s))

print('s:', len(s))
print('s_hat:', len(s_hat))

s_x = []
s_y = []
for i in s:
    s_x.append(x[i - 1])
    s_y.append(y[i - 1])

s_hat_x = []
s_hat_y = []
for i in s_hat:
    s_hat_x.append(x[i - 1])
    s_hat_y.append(y[i - 1])

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(s_x, s_y, marker='o', linestyle='None', color='green')
ax.plot(s_hat_x, s_hat_y, marker='o', linestyle='None', color='red')
for i, j in edges.keys():
    ax.plot([x[int(i) - 1], x[int(j) - 1]], [y[int(i) - 1], y[int(j) - 1]],
            color='#66ccff')
plt.show()
