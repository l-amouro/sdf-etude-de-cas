import math
from scipy.linalg import expm
from scipy.linalg import null_space

import numpy as np
lambda_GE=2*10**-3
lambda_s_1 = lambda_GE
lambda_s_2 = 0.1 * lambda_GE
lambda_s_3 = 0

MTTR=24
mu_GE=1/MTTR
mu_vide=0

A_temp_2crew_s_1 = np.array([[0, 2*mu_GE, 0], [lambda_GE, 0, mu_GE], [0, lambda_GE+lambda_s_1, 0]])
A_temp_2crew_s_2 = np.array([[0, 2*mu_GE, 0], [lambda_GE, 0, mu_GE], [0, lambda_GE+lambda_s_2, 0]])
A_temp_2crew_s_3 = np.array([[0, 2*mu_GE, 0], [lambda_GE, 0, mu_GE], [0, lambda_GE+lambda_s_3, 0]])

A_temp_2crew_s_1_vide = np.array([[0, 2*mu_vide, 0], [lambda_GE, 0, mu_vide], [0, lambda_GE+lambda_s_1, 0]])
A_temp_2crew_s_2_vide = np.array([[0, 2*mu_vide, 0], [lambda_GE, 0, mu_vide], [0, lambda_GE+lambda_s_2, 0]])
A_temp_2crew_s_3_vide = np.array([[0, 2*mu_vide, 0], [lambda_GE, 0, mu_vide], [0, lambda_GE+lambda_s_3, 0]])

def remplir_diag(A):
    for i in range(len(A)):
        A[i][i] = -(sum(A[i]) - A[i][i])
    return A

A_2crew_s_1 = remplir_diag(A_temp_2crew_s_1)
A_2crew_s_2 = remplir_diag(A_temp_2crew_s_2)
A_2crew_s_3 = remplir_diag(A_temp_2crew_s_3)

A_2crew_s_1_vide = remplir_diag(A_temp_2crew_s_1_vide)
A_2crew_s_2_vide = remplir_diag(A_temp_2crew_s_2_vide)
A_2crew_s_3_vide = remplir_diag(A_temp_2crew_s_3_vide)

def trim_A(A, state):
    Q = np.copy(A)
    Q = np.delete(Q, state, axis=0)
    Q = np.delete(Q, state, axis=1)
    return Q

def get_Q(A, state):
    Q = trim_A(A, state)
    Q = np.flip(Q)
    return Q

print("pour mu = 1/24, lambda_s = 0.5lambda, MTTF =", np.linalg.solve(-get_Q(A_2crew_s_1,0), np.ones(2))[0])
print("pour mu = 1/24, lambda_s = 0.1lambda, MTTF =", np.linalg.solve(-get_Q(A_2crew_s_2,0), np.ones(2))[0])
print("pour mu = 1/24, lambda_s = 0, MTTF =", np.linalg.solve(-get_Q(A_2crew_s_3,0), np.ones(2))[0])

print("pour mu = 0, lambda_s = 0.5lambda, MTTF =", np.linalg.solve(-get_Q(A_2crew_s_1_vide,0), np.ones(2))[0])
print("pour mu = 0, lambda_s = 0.1lambda, MTTF =", np.linalg.solve(-get_Q(A_2crew_s_2_vide,0), np.ones(2))[0])
print("pour mu = 0, lambda_s = 0, MTTF =", np.linalg.solve(-get_Q(A_2crew_s_3_vide,0), np.ones(2))[0])


P_t_0=np.array([1,0])
t_miss=24

print("R(24h) pour mu = 1/24, lambda_s = 0.5lambda", P_t_0 @ expm(get_Q(A_2crew_s_1,0) * t_miss) @ [[1],[1]])
print("R(24h) pour mu = 1/24, lambda_s = 0.1lambda", P_t_0 @ expm(get_Q(A_2crew_s_2,0) * t_miss)@ [[1],[1]])
print("R(24h) pour mu = 1/24, lambda_s = 0", P_t_0 @ expm(get_Q(A_2crew_s_3,0) * t_miss)@ [[1],[1]])

print("R(24h) pour mu = 0, lambda_s = 0.5lambda", P_t_0 @ expm(get_Q(A_2crew_s_1_vide,0) * t_miss)@ [[1],[1]])
print("R(24h) pour mu = 0, lambda_s = 0.1lambda", P_t_0 @ expm(get_Q(A_2crew_s_2_vide,0) * t_miss)@ [[1],[1]])
print("R(24h) pour mu = 0, lambda_s = 0", P_t_0 @ expm(get_Q(A_2crew_s_3_vide,0) * t_miss)@ [[1],[1]])
