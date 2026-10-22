import math

q={}

tau_jour = 24
tau_mois = 730
tau_6_mois = 4380
tau_annee = 8760

lambda123 = [2e-6, 1e-6, 5e-6]

for ge in [1, 2, 3]:
    lambda_temp = lambda123[ge-1]
    q_val = lambda_temp * tau_mois / 2
    for sub in ['a', 'b']:
        q[f'{ge}{sub}'] = q_val

for sub in ['a', 'b']:
        q[f'{4}{sub}'] = 1e-3

q['5'] = 5e-4

lambda67 = [5e-4, 1.5e-3]
for ge in [6,7]:
    lambda_temp = lambda67[ge-6]
    q_val = 1 - math.exp(-lambda_temp * tau_jour)
    for sub in ['a', 'b']:
        q[f'{ge}{sub}'] = q_val

q['8'] = 1e-3
q['11'] = 1 - math.exp(-1e-6 * tau_jour)
q['13'] = 1 - math.exp(-1e-5 * tau_jour)
q['14'] = 1 - math.exp(-1e-5 * tau_jour)
q['15'] = 1e-6 * tau_6_mois / 2
q['16'] = 1 - math.exp(-1e-7 * tau_jour)
q['17'] = 1 - math.exp(-2e-5 * tau_jour)
q['18'] = 1e-6 * 8760 / 2
q['19'] = 1e-3
q['20'] = 2e-6 * 4380 / 2
q['21'] = 1e-4
q['CC'] = 1 - math.exp(-1e-5 * tau_jour)

#2°)
liste_coupe_minimales = []
num_commun = [1,2,3,4,6,7]
for i in num_commun:
     for j in num_commun:
          liste_coupe_minimales.append([f'{i}a', f'{j}b'])
liste_coupe_minimales.append(['5'])
liste_coupe_minimales.append(['8'])
liste_coupe_minimales.append(['11'])
liste_coupe_minimales.append(['13'])
liste_coupe_minimales.append(['17'])
liste_coupe_minimales.append(['16'])
liste_coupe_minimales.append(['15'])
liste_coupe_minimales.append(['CC','18'])
liste_coupe_minimales.append(['CC','19'])
liste_coupe_minimales.append(['14','20'])
liste_coupe_minimales.append(['21'])

print("Il y a bien", len(liste_coupe_minimales), "coupes minimales:", )

#3°)
Q_chapeau_j_coupe_minimales = []
for coupe in liste_coupe_minimales:
    q_chapeau_j = 1
    for i in coupe:
        q_chapeau_j *= q[i]
    Q_chapeau_j_coupe_minimales.append((coupe,q_chapeau_j))

p_top_rare = 0
for coupe in Q_chapeau_j_coupe_minimales:
    p_top_rare += coupe[1]
print("La probabilité de l'événement top rare est:", p_top_rare)
p_upper_bound=0
temp = 1
for coupe in Q_chapeau_j_coupe_minimales:
    temp *= 1 - coupe[1]
    
p_upper_bound = 1 - temp
print("La borne supérieure de la probabilité de l'événement top rare est:", p_upper_bound)
#4)°
def OU(*p):
    return 1 - math.prod([1 - x for x in p])
def ET(*p):
    return math.prod(p)

def top(q):
    G4=OU(q['18'],q['19'])
    G3=ET(q['CC'], G4)
    G1 = OU(q['16'],G3)
    G5 = OU(q['8'],q['11'])
    G9 = ET(q['14'],q['20'])
    G10 = OU(q['15'],q['13'])
    G11 = OU(q['17'],q['5'],q['21'])
    GE1 = OU(q['1a'],q['2a'],q['3a'],q['4a'],q['6a'],q['7a'])
    GE2 = OU(q['1b'],q['2b'],q['3b'],q['4b'],q['6b'],q['7b'])
    G12 = ET(GE1,GE2)
    G7 = OU(G9, G10)
    G8 = OU(G11, G12)
    G6 = OU(G7, G8)
    G2 = OU(G5, G6)
    G0 = OU(G1, G2)
    return G0
print("top(q):", top(q))
print("L'approximation top rare est proche de la valeur exacte d'un %", abs(top(q)-p_top_rare)/top(q)*100)
print("L'approximation upperbound est proche de la valeur exacte d'un %", abs(top(q)-p_upper_bound)/top(q)*100)
#5°)
Q_chapeau_j_coupe_minimales_tri = sorted(Q_chapeau_j_coupe_minimales, key=lambda x: x[1], reverse=True)
top5 = Q_chapeau_j_coupe_minimales_tri[:5]
print("Les 5 coupes minimales les plus probables sont:")
for coupe in top5:
    print(coupe[0], "avec une probabilité de", coupe[1])

#Day2 2°)
Birnbaum = {}
Fussell_Vesely = {}
for i in q.keys():
    q_zeros = q.copy()
    q_ones = q.copy()
    q_zeros[i] = 0
    q_ones[i] = 1
    Birnbaum[i] = top(q_ones) - top(q_zeros)
    Fussell_Vesely[i] = (top(q)-top(q_zeros))/top(q)

#sort Fussell_Vesely by value
Fussell_Vesely_sorted = sorted(Fussell_Vesely.items(), key=lambda
    x: x[1], reverse=True)

#print the sorted Fussell_Vesely
print("Fussell_Vesely sorted:")
for i in Fussell_Vesely_sorted:
    print(i[0], ": FV:", i[1], "Birnbaum:", Birnbaum[i[0]])




