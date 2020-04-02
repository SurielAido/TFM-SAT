import random


class Walksat:

    def isset(variable):
        return variable in locals() or variable in globals()

    def walksat(self, formula, max_tries, max_flips, p):
        for i in range(max_tries):
            assignement = self.randomAssignement(formula)
            for j in range(max_flips):
                if self.thisFormIsSatisfied(assignement):
                    return assignement
                else:

        return False

    def randomAssignement(formula):
        cnf = []
        formuAndAssig = {}
        keys = tuple(formuAndAssig.keys())
        keyslist = []
        for forms in formula:
            for v in forms:
                clause = []
                if v not in keys and v != 0:
                    formuAndAssig[v] = bool(random.getrandbits(1))
                    if v not in keyslist:
                        keyslist.append(v)
                else:
                    continue
            for k in keyslist:
                if k in forms:
                    k = 1 if formuAndAssig.get(k) else 0
                    clause.append(k)
                else:
                    continue
            cnf.append(clause)
        return cnf

    def thisFormIsSatisfied(cnfAssignement):
        result = False
        acum = 0
        for i in cnfAssignement:
            acumPorForm = 0
            for j in i:
                acumPorForm += j
            if acumPorForm > 1:
                acum += 1
        if acum < len(cnfAssignement):
            result = False
        else:
            result = True
        return result
