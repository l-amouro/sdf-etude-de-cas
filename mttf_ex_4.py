import math

def k_sur_n(k, n, R):
    R_sys = 0
    for i in range(k, n + 1):
        R_sys += math.comb(n, i) * (R ** i) * ((1 - R) ** (n - i))
    return R_sys

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def is_greater(f, g):
    i=0
    while f(i) >= g(i):
        i+=1
    return i


list_l_1Gen = [2*10**(-3)]
list_R_24_1Gen = [math.exp(-l * 24) for l in list_l_1Gen]

#on choisit l'intervalle de temps [0, 10000] car il est significativement plus grand que la MTTF attendue du système, ce qui permet de capturer la majorité de la distribution de fiabilité et d'obtenir une estimation précise de la MTTF. L'intervalle est divisé en 10000 sous-intervalles pour assurer une approximation précise de l'intégrale.
print("MTTF for a 1 out of 2 system with lambda = 2*10**(-3): ", trapezoidal_rule(lambda t: k_sur_n(1, 2, math.exp(-2*10**(-3) * t)), 0, 10000, 10000))
print("MTTF for a 2 out of 3 system with lambda = 2*10**(-3): ", trapezoidal_rule(lambda t: k_sur_n(2, 3, math.exp(-2*10**(-3) * t)), 0, 10000, 10000))
print("MTTF for a 1 out of 1 system with lambda = 2*10**(-3): ", trapezoidal_rule(lambda t: k_sur_n(1, 1, math.exp(-2*10**(-3) * t)), 0, 10000, 10000))
print("temps où R 2 sur 3 devient inférieur à R 1 générateur: ", is_greater(lambda t: k_sur_n(2, 3, math.exp(-2*10**(-3) * t)), lambda t: k_sur_n(1, 1, math.exp(-2*10**(-3) * t))))