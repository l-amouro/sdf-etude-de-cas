import math
from scipy.linalg import expm
from scipy.linalg import null_space

import numpy as np
lambda_GE=2*10**-3
MTTR=24
mu_GE=1/MTTR

A_temp_2crew = np.array([[-2*mu_GE, 2*mu_GE, 0], [lambda_GE, -(mu_GE+lambda_GE), mu_GE], [0, 2*lambda_GE, -2*lambda_GE]])
A_temp_1crew = np.array([[-mu_GE, mu_GE, 0], [lambda_GE, -(mu_GE+lambda_GE), mu_GE], [0, 2*lambda_GE, -2*lambda_GE]])

def remplir_diag(A):
    for i in range(len(A)):
        A[i][i] = -(sum(A[i]) - A[i][i])
    return A

A_2crew = remplir_diag(A_temp_2crew)
A_1crew = remplir_diag(A_temp_1crew)

#solve the system P*A = 0, sum (P) = 1 to find the steady state probabilities

def compute_steady_state(A):
    ns = null_space(A.T)
    x = ns[:, 0]
    x = x / np.sum(x)
    return x

availability_array = np.array([0, 1, 1])
P_2crew = compute_steady_state(A_2crew)
P_1crew = compute_steady_state(A_1crew)
availability_2crew = np.dot(P_2crew, availability_array)
availability_1crew = np.dot(P_1crew, availability_array)
unavailability_2crew = 1 - availability_2crew
unavailability_1crew = 1 - availability_1crew

print("Steady state probabilities 2crew:", P_2crew)
print("Steady state probabilities 1crew:", P_1crew)
print("Availability 2crew:", availability_2crew)
print("Availability 1crew:", availability_1crew)
print("Unavailability 2crew:", unavailability_2crew)
print("Unavailability 1crew:", unavailability_1crew)


P0 = np.array([0, 0, 1])
def compute_P(A, t):
    P = P0 @ expm(A * t)
    return P

print("P(24h) 2crew =", compute_P(A_2crew, 24))
print("P(100h) 2crew =", compute_P(A_2crew, 100))
print("P(1000h) 2crew =", compute_P(A_2crew, 1000))
print("P(24h) 1crew =", compute_P(A_1crew, 24))
print("P(100h) 1crew =", compute_P(A_1crew, 100))
print("P(1000h) 1crew =", compute_P(A_1crew, 1000))
