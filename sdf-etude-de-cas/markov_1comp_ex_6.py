import math
from scipy.linalg import expm
import numpy as np
lambda_GE=2*10**-3
MTTR=24
mu_GE=1/MTTR

A_temp = np.array([[0, lambda_GE], [mu_GE, 0]])
def remplir_diag(A):
    for i in range(len(A)):
        A[i][i] = -(sum(A[i]) - A[i][i])
    return A

#compute P(t) = P(0)·expm(A·t) with scipy.linalg.expm, for t = 24, 100 and 1000 h

A = remplir_diag(A_temp)
P0 = np.array([1, 0])

def compute_P(t):
    P = P0 @ expm(A * t)
    return P

print("P(24h) =", compute_P(24))
print("P(100h) =", compute_P(100))
print("P(1000h) =", compute_P(1000))

#compare it with the analytic A(t) = μ/(λ+μ) + λ/(λ+μ)·e^(−(λ+μ)t)

def analytic_A(t):
    return mu_GE/(lambda_GE + mu_GE) + lambda_GE/(lambda_GE + mu_GE) * math.exp(-(lambda_GE + mu_GE) * t)

print("Analytic A(24h) =", analytic_A(24))
print("Analytic A(100h) =", analytic_A(100))
print("Analytic A(1000h) =", analytic_A(1000))

print("A_infinity =", mu_GE/(lambda_GE + mu_GE))
print("A_infinity_approx =", analytic_A(1000000))


