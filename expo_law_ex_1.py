#Program to calculate using Python different values of RAMS analysis for an exponential law

import math


def MTTF(l):
	return 1 / l

def R24h(l):
    return math.exp(-l * 24)

l = 2*10**(-3)
print("MTTF: ", MTTF(l))
print("Reliability after 24 hours: ", R24h(l))
