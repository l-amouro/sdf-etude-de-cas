import math
from scipy.linalg import expm
from scipy.linalg import null_space
import numpy as np

lambda_GE=2*10**-3
MTTR=24
mu_GE=1/MTTR
mu_vide = 0

A_temp_2crew = np.array([[-2*mu_GE, 2*mu_GE, 0], [lambda_GE, -(mu_GE+lambda_GE), mu_GE], [0, 2*lambda_GE, -2*lambda_GE]])
A_temp_1crew = np.array([[-mu_GE, mu_GE, 0], [lambda_GE, -(mu_GE+lambda_GE), mu_GE], [0, 2*lambda_GE, -2*lambda_GE]])
A_temp_sans_repar = np.array([[-2*mu_vide, 2*mu_vide, 0], [lambda_GE, -(mu_vide+lambda_GE), mu_vide], [0, 2*lambda_GE, -2*lambda_GE]])

def remplir_diag(A):
    for i in range(len(A)):
        A[i][i] = -(sum(A[i]) - A[i][i])
    return A

A_2crew = remplir_diag(A_temp_2crew)
A_1crew = remplir_diag(A_temp_1crew)
A_sansrepar = remplir_diag(A_temp_sans_repar)

def trim_A(A, state):
    Q = np.copy(A)
    Q = np.delete(Q, state, axis=0)
    Q = np.delete(Q, state, axis=1)
    return Q

def get_Q(A, state):
    Q = trim_A(A, state)
    Q = np.flip(Q)
    return Q

T = np.linalg.solve(-get_Q(A_2crew,0), np.ones(2))
print("pour mu = 1/24, T =", T)

T_vide = np.linalg.solve(-get_Q(A_sansrepar,0), np.ones(2))
print("pour mu = 0, T =", T_vide)

print("MTTF avec réparations est ", T[0]/T_vide[0], " fois plus grande")