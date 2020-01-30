import random


class Walksat:

    def isset(variable):
        return variable in locals() or variable in globals()

    def walksat(self, formula, max_tries, max_flips, p):
        cnfRes = 0
        cnf = []
        formuAndAssig = {}
        for i in range(max_tries):
            n = 0
            m = 0
            for j in formula:
                acum = 0
                for k in formula[n]:
                    if(self.isset(formula)):
                        if formula[n][k] in cnf[n-1]:
                            formula[n][k] = cnf[n-1][k-1]
                            continue
                        else:
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



    # def walksat(formula, max_tries, max_flips, p):
    #     cnfRes = 0
    #     cnf = []
    #     formuAndCnf = {}
    #     for i in range(max_tries):
    #         n = 0
    #         for k in formula:
    #             acum = 0
    #             cnfAux = []
    #             for s in formula[n]:
    #                 s = bool(random.getrandbits(1))
    #                 s = 0 if s == False else 1
    #                 acum = acum + s
    #                 cnfAux.append(s)
    #             if acum >= 1:
    #                 result = True
    #             else:
    #                 result = False
    #             if result:
    #                 cnfRes += 1
    #             cnf.append(cnfAux)
    #             n = n + 1
    #         for x in range(len(cnf)):
    #             formuAndCnf[tuple(formula[x])] = cnf[x]
    #         print("Fórmula en relación con CNF => ", formuAndCnf)
    #         for j in range(max_flips):
    #             if cnfRes >= len(formula):
    #                 print("¿La asignación satisface la fórmula? ", True)
    #                 print("La asignación es la siguiente: ", cnf)
    #                 return cnf, True
    #             else:
    #                 i = 1
    #                 aux = {}
    #                 for l in cnf:
    #                     # print("Cláusula", l)
    #                     if sum(l) == 0:
    #                         aux[i] = l;
    #                     i += 1
    #                 print("Cláusula no satisfecha", aux)
    #                 # ran = random.randrange(len(aux))
    #                 # chosen = aux[ran]
    #                 # for l in cnf:
    #                 #     if chosen == l:
    #                 #         for l2 in chosen:
    #                 #             l2 *= -1
    #                 #
    #
    #                 print("La fórmula es insatisfastible")
    #                 return [], False
