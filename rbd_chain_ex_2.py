
import math 

def serie(list_of_R):
    R_sys = 1
    for i in list_of_R:
        R_sys = R_sys * i
    return R_sys

def parallele(list_of_R):
    R_sys = 1
    for i in list_of_R:
        R_sys = R_sys * (1 - i)
    return 1 - R_sys


list_l_series = [1*10**(-5), 5*10**(-5), 1*10**(-6)]
list_l_parallele = [2*10**(-3), 2*10**(-3)]
list_l_parallele_1Gen = [2*10**(-3)]

list_R_series_24 = [math.exp(-l * 24) for l in list_l_series]
list_R_parallele_24 = [math.exp(-l * 24) for l in list_l_parallele]
list_R_parallele_24_1Gen = [math.exp(-l * 24) for l in list_l_parallele_1Gen]


print("Reliability after 24 hours for the system: ", serie(list_R_series_24) * parallele(list_R_parallele_24))
print("Reliability after 24 hours for the system: ", serie(list_R_series_24) * parallele(list_R_parallele_24_1Gen))