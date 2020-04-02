from Utilities.utilities import Utilities
from Algorithms.walksat import Walksat

walk = Walksat()
# nVariables, formulaLen, clauseLen
form = Utilities.random_generator(7, 6, 5)  # Si quitamos los 0 tarda mucho en hacerlo,
                                            # ya que con números bajos le cuesta mucho satisfacer las restricciones.
# form = Utilities.random_generator(5, 6, 5)
# form = [[0, 0, 1], [0, 1, 0], [1, 1, 0]]
Walksat.walksat(form[0], 1, 4, 0.5)

