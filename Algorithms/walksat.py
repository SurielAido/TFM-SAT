import random


class Walksat:

    def walksat(formula, max_tries, max_flips, p):
        cnfRes = 0
        cnf = []
        for i in range(max_tries):
            n = 0
            for k in formula:
                acum = 0
                cnfAux = []
                for s in formula[n]:
                    s = bool(random.getrandbits(1))
                    s = 0 if s == False else 1
                    acum = acum + s
                    cnfAux.append(s)
                if acum >= 1:
                    result = True
                else:
                    result = False
                if result:
                    cnfRes += 1
                cnf.append(cnfAux)
                n = n + 1
            for j in range(max_flips):
                if cnfRes >= len(formula):
                    print("¿La asignación satisface la fórmula? ", True)
                    print("La asignación es la siguiente: ", cnf)
                    return cnf, True
                else:
                    aux = []
                    for l in cnf:
                        print(l)
                        if sum(l) == 0:
                            aux.append(l);
                    ran = random.randrange(len(aux))
                    chosen = aux[ran]
                    for l in cnf:
                        if chosen == l:
                            for l2 in chosen:
                                l2 *= -1


                    print("La fórmula es insatisfastible")
                    return [], False
