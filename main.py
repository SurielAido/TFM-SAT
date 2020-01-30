from Utilities.utilities import Utilities
from Algorithms.walksat import Walksat

# nVariables, forLen, clausLen
form = Utilities.random_generator(5, 6, 3)
# form = [[0, 0, 1], [0, 1, 0], [1, 1, 0]]
Walksat.walksat(form, 4, 4, 0.5)

