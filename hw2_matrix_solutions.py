from sympy import *

9. 
def get_determinant(M):

	if M.length <= 10:
		determinant_value = M.det()

return determinant_value

10. ?

11. 
M = Matrix([[4, 3, 2], [1, 2, 6], [5, 8, 1]])
M.eigenvals()
M.eigenvects()