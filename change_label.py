import numpy as np

path = './SEGEMENTED.txt'
mat = np.loadtxt(path)
mat[..., -1] = 5.

np.savetxt(path,  mat, fmt='%.3f')