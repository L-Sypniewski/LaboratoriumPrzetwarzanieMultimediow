# -*- coding: utf-8 -*-
"""

Laboratorium z Przetwarzania multimediów
sem. 2018/2019
Autor: Marcin Wilczewski
"""
# =============================================================================
# Koniecznie: 
#           https://docs.scipy.org/doc/numpy/user/quickstart.html 
#           http://www.scipy-lectures.org/intro/matplotlib/index.html
# Opcjonalnie:
# ftp://ftp.cea.fr/pub/unati/people/educhesnay/pystatml/StatisticsMachineLearningPythonDraft.pdf
# 
# =============================================================================

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

#uwaga na zakresy range (lewostronnie domkniety, prawostronnie otwarty)
a = np.array(range(1,100))
a


a = np.array([1,2,3,4,5,6,7,8,9])
a.shape
a = a.reshape((3,3))
a.shape
a
type(a)
a.shape

#Tworzenie struktury
#help: np.arange?: [start,stop)
# np.arange?
#tworzenie struktury (tablicy)
a = np.array(range(0,100))
#lub rownowaznie, ale krocej
a = np.arange(0,100)

# np.linspace?
a = np.arange(0,10,0.5) #tak jak range (array range)
a = np.linspace(0,10,9)
a = np.linspace(0,10,4) 

#operacje na strukturach nie są wykorzystywane "in line"
a = np.linspace(0,10,27)
a.reshape(3,3,3) #nie wywołuje zmiany struktury a
a = a.reshape(3,3,3)

a.ndim
a.shape
a.size

#spłaszczanie struktury flatten <-> reshape
a = a.reshape(3,9)
a.shape
a = a.flatten()
a.shape


a = np.array([1,2])
b = np.array([3,4])
c = np.array((5,6))

#odpowiedniki rbind oraz cbind w R
# np.stack?
d = np.stack((a,b,c),axis=0)
d
d = np.stack((a,b,c),axis=1)
d



#selekcja i wycinanie
a = np.arange(0,100).reshape((10,10))
a
a[:,:]
a[:,5]
a[5,:]
a[1,2:5] #zwroc uwage na zakres prawostronnie otwarty

a
a[0,2:]
a[0,:2]
a[3:6,3:6]
a[::-1,0]

#poniższa instrukcja nie tworzy kopii, ale wskazuje na obszar pamięci
a2 = a[:,0] 
a2
a2[0]=999
print(a)
print(a2)

#poniższa instrukcja tworzy kopię
a = np.arange(0,100).reshape(10,10)
a3 = a[:,[0]]
a3
a3[0]=999
a



# =============================================================================
# Tworzenie macierzy
# =============================================================================
mat = np.ones((5,5))
mat.trace()
mat.T


#Macierzj jednostkowa
mat = np.identity(5)
mat = np.eye(5)

#Macierze zer i jedynek
mat = np.zeros((5,5))
mat = np.ones((5,5))

#Główna przekątna
mat = np.diag([1,2,3,4,5])
np.diag(mat)
np.lookfor("diag")


#Wektoryzacja w numpy. Wektoryzacja wykonywanie działań element-po-elemencie
mat = np.random.randint(0,100,(7,7))
mat = np.random.randint(0,100,49)
mat*2
mat * mat
np.sin(mat)
sin(mat)# to sie nie powiedzie

#testy logiczne element po elemencie
mat>50
mat[mat>50]

mat
mat[mat>50] = 999
mat
mat == 50
mat!=50
mat != 50
mat != 50
mat[mat != 50]
mat 
(mat <10) | (mat > 90)
mat[(mat<10) | (mat>90)] = -999
mat

mat = np.sqrt(mat)
np.isnan(mat)

#Przykład: odległosc Manhattan oraz Euklidesa
a = np.random.randint(0,99,5)
b = np.random.randint(0,99,5)
manhattan = np.sum(np.abs(a-b))
eukl = np.sqrt(np.sum((a-b)**2))
np.argmin(a)

#iloczyn skalarny
vec1 = np.random.randint(0,10,10)
vec2 = np.random.randint(0,10,10)
vec1.dot(vec2)
sum(vec1*vec2)

#Generatory liczb pseudolosowych
# https://docs.scipy.org/doc/numpy/reference/routines.random.html


# =============================================================================
# Wykresy 
# =============================================================================
# import matplotlib.pyplot as plt
# x = np.arange(-2*np.pi, 2*np.pi,0.05)
# y = np.sin(x)
# plt.plot(x,y)
