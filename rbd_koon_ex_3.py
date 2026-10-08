import math

def serie(list_of_R):
    R_sys = 1
    for i in list_of_R:
        R_sys = R_sys * i
    return R_sys

def k_sur_n(k, n, R):
    R_sys = 0
    for i in range(k, n + 1):
        R_sys += math.comb(n, i) * (R ** i) * ((1 - R) ** (n - i))
    return R_sys


list_l_series = [1*10**(-5), 5*10**(-5), 1*10**(-6)]
list_R_series_24 = [math.exp(-l * 24) for l in list_l_series]
list_l_1Gen = [2*10**(-3)]
list_R_24_1Gen = [math.exp(-l * 24) for l in list_l_1Gen]
print("Reliability after 24 hours for the system: ", serie(list_R_series_24) * k_sur_n(2, 3, list_R_24_1Gen[0]))
print("Reliability after 24 hours for the system: ", serie(list_R_series_24) * k_sur_n(1, 2, list_R_24_1Gen[0]))
print("Reliability after 24 hours for the system: ", serie(list_R_series_24) * k_sur_n(3, 3, list_R_24_1Gen[0]))
print("Reliability after 24 hours for the system: ", serie(list_R_series_24) * serie(list_R_24_1Gen)*serie(list_R_24_1Gen)*serie(list_R_24_1Gen))


