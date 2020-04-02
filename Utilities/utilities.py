import random


class Utilities:

    #Quitar el valor 0 de la fórmula.

    def random_generator(nVariables, forLen, clausLen):
        formula = []
        # print("Venga, la fórmula en estado original ", formula)
        clause = []
        # print("Venga, la clásula en estado original ", clause)
        trivial = False
        simplifiable = False
        formula_string = ''
        while len(formula) < forLen:
            clause = []
            for j in range(clausLen):
                # print("Iteración nº",j)
                v = random.randrange(1, nVariables)
                # print("Vamos a ver el random v: ", v)
                if bool(random.getrandbits(1)):
                    v *= -1
                clause.append(v)
                # print("Vamos a ver la cláusula después del append v", clause)
            cont = 0
            for c in clause:
                cont = clause.count(c)
                if cont > 1:
                    simplifiable = True
                    break
                else:
                    simplifiable = False
                if (c in clause) and ((c * -1) in clause) and c != 0:
                    trivial = True
                    break
                else:
                    trivial = False

                # print("Vamos a ver el simplifiable: ", simplifiable)
                # print("Vamos a ver el trivial: ", trivial)
            if not trivial and not simplifiable:
                clause.append(0)
                formula.append(clause)
        for i in range(len(formula)):
            strConv = ""
            for c in formula[i]:
                if str(c) == '0':
                    c = '\n'
                    strConv += str(c)
                else:
                    strConv += str(c) + ' '
                aux = (strConv)
            formula_string += aux
        # print("Tenemos una fórmula de longitud ",  forLen, ".")
        # print("Tenemos ", clausLen, " cláusulas que vamos a intentear formar.")
        # print("Tenemos ", nVariables, " variables.")
        # print('Prueba:\n', formula_string)
        print("La fórmula resultado es: ", formula)
        return formula, formula_string
