from math import *
import numpy as np


#Tworzenie struktury 
#Tworzenie struktury
#numpy umożliwia tworzenie obiektów tablicowych ndarray
a = np.array([1,2,3,4,5,6])
type(a)
print(a)
lista = [1,2,3,4,5,6]
type(lista)
print(np.sin(a))

#obiekty ndarray umożliwiają wektoryzację działań
# lista+2
a+2

np.sin(a) # ok. Instrukcje z pakietu numpy umozliwiają wykonywanie dzialan na obiektach ndarray
# sin(a)    # blad


print(a.shape)
a = np.array([[1,2],[3,4]])
print(a)
print(a.shape)