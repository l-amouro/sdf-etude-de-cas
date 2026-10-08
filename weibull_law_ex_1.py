#Program to calculate using Python different values of RAMS analysis for a weibull law

import math
import expo_law_ex_1


def theta(alpha, MTTF):
    return MTTF / math.gamma(1 + 1/alpha)

def R24h(alpha, theta):
    return math.exp(-((24/theta)**alpha))

MTTF = expo_law_ex_1.MTTF(2*10**(-3))

print("scale :", theta(1.5, MTTF))
print("Reliability after 24 hours:", R24h(1.5, theta(1.5, MTTF)))