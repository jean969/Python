import numpy as np 
matrix_a = np.array([ [0,1,2], [4,5,6], [10,5,7]])
matrix_b = np.array([ [2,4,6,7], [10,20,4,20], [1,-1,4,6]])

# calcul de matrix_a * matrix_b 

produit = np.dot(matrix_a, matrix_b)
print("\n matrix_a * matrix_b =\n", produit)


 #calcul de la transposé de la matrix_a
transposé = matrix_a.T 
print("\n transposé de la matrix_a est =\n", transposé)
 
# calcul de determinant de la matrix_a 
def determinant_matrix_a (a,b,c,d,e,f,g,h,i):
    return a*e*f + b*g*i + c*d*h - c*e*g - b*d*i - a*f*h
det = determinant_matrix_a(0,1,2,
                           4,5,6, 
                           10,5,7)
print("Determinant de la matrix_a est",det)

#calul de l'inversibilité de la matrix_a
if det != 0:
    print("La matrix_a est inversible")
    print("Dans le cas ou la matrix_a est inversible, son inverse est :")
    invverse_marix_a = (1/det) * np.array([[7,-6,2],[-5,5,-1],[10,-4,0]])
    print(invverse_marix_a)
else:
    print("La matrix_a n'est pas inversible")

#calul de l'inversibilité de la matrix_a par sa transposé 
print("calul de l'inversibilité de la matrix_a par sa transposé")
print("Dans le cas ou la matrix_a est inversible, son inverse est :")
invverse_marix_a = (1/det) * transposé
print(invverse_marix_a)
