from numpy import array, polymul, polydiv
from sympy import symbols, poly

def reedSolomonEncode(wordToEncode):
    #Encodage du mot
    roots = [1,2]
    encodedWord = []
    for i in range(len(wordToEncode)):
        encodedWord.append(ord(wordToEncode[i]))

    #Construction du polynôme principal
    polynom = array(encodedWord)
    polynom = polymul(polynom, array([1]))

    #Construction du polynôme générateur
    x = symbols('x')
    expression = (x - roots[0]) * (x - roots[1])
    expanded_expression = poly(expression)
    poly_coeffs = expanded_expression.all_coeffs()
    poly_attributes = array(poly_coeffs)
    generatorPolynomial = []
    for j in range (len(poly_attributes)) :
        generatorPolynomial.append(int(poly_attributes[j]))

    #Division des deux polynômes
    q, r = polydiv(polynom, array(generatorPolynomial))
    remainder = [int(f) for f in r]

    #Retourne le polynôme du message et le reste de la division
    return polynom.tolist() + remainder
