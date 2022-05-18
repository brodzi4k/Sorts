import pandas as pd
import time
import statistics
import math
import random

# plik z danymi na gicie jest w xls, a nie w csv  
# ponieważ csv zajmowal 39MB 
data= pd.read_csv('projekt2_dane2.csv', sep=';')
data2 = data.rating.to_list()
data3 = data.movie.to_list()
data4 = data.id.to_list()
lista2 = []
lista3 = []
lista4 = []
indeksy = []

# zakresy danych
zakresTest = 10
zakres1 = 10000
zakres2 = 100000
zakres3 = 500000
zakres4 = 1000000
zakres5 = 1010293


zakres = zakres1
data2 = data2[0:zakres]
data3 = data3[0:zakres]
data4 = data4[0:zakres]
a = 0
dlugosc = len(data2)
for i in range(dlugosc):
    #print(data2[i])
    data2[i] = str(data2[i])
    #print(i)
    if data2[i] != 'nan':
        lista2.append(float(data2[i]))
        lista3.append(data3[i])
        lista4.append(data4[i])
    else:
        pass

#print(len(lista2))
#print(len(lista3))
#print(len(lista4))


indeksy = []

def quick_sort(L):


    if len(L) <= 1:
        return L

    # pobieranie pivota wg ktorego bedziemy operowac
    pivot = L[0]
    less = []


    # wszystkie mniejsze elementy od pivot przerzucamy do listy mniejszych
    for x in L:
        if x < pivot:
            less.append(x)
            # print(less.append(x))
            indeksy.append(less.index(x))

    # wszystkie rowne elementy przerzucamy do listy rownych
    equal = []
    for x in L:
        if x == pivot:
            equal.append(x)

    # wszystkie wiesze elementy od pivot przerzucamy do listy wiekszych
    greater = []
    for x in L:
        if x > pivot:
            greater.append(x)
            indeksy.append(greater.index(x))

    # ponawiamy procedure dla mniejszych i wiekszych elementow
    return quick_sort(less) + equal + quick_sort(greater)


dict1 = {}
for a in range(len(lista2)):
    dict1[lista3[a]] = lista2[a]


#test gotowego algorytmu w celu porownania czasu

#dupa1 = sorted(dict1.items(), key=lambda x: x[1])
#print(dupa1)


# operacja scalania
def merge(L, start, center, finish):

    i = start
    j = center + 1

    L2 = []  # lista pomocnicza

    # wybieraj odpowiednie elementy z dwoch tablic
    while (i <= center) and (j <= finish):
        if L[j] < L[i]:
            L2.append(L[j])
            j = j + 1
        else:
            L2.append(L[i])
            i = i + 1

    # koniec tablicy ? = przepisz reszte z pozostalej
    if i <= center:
        while i <= center:
            L2.append(L[i])
            i = i + 1
    else:
        while j <= finish:
            L2.append(L[j])
            j = j + 1

    # przepisanie z tablicy tmp
    s = finish - start + 1
    i = 0
    while i < s:
        L[start + i] = L2[i]
        i = i + 1

    return L


# sortowanie przez scalanie
def merge_sort(L, start, finish):

    if start != finish:

        center = int(math.floor((start + finish) / 2))
    # na lewo
        merge_sort(L, start, center)
        # na prawo
        merge_sort(L, center + 1, finish)

        # operacja scalania
        merge(L, start, center, finish)
    return L


def bucketSort(array, noOfBuckets):
    noOfBuckets = 10
    max_ele = zakres
    min_ele = 0

    # Zakres kubelkow
    rngeOfBuckets = (max_ele - min_ele) / noOfBuckets

    temp = []

    # Utworzenie pustych kubelkow
    for i in range(noOfBuckets):
        temp.append([])

    # Sortowanie tablicy na kubelki
    for i in range(len(array)):
        queue = (array[i] - min_ele) / rngeOfBuckets - int((array[i] - min_ele) / rngeOfBuckets)

    # Elementy graniczne wrzucamy do tablicy tablice nizej
        if (queue == 0 and array[i] != min_ele):
            temp[int((array[i] - min_ele) / rngeOfBuckets) - 1].append(array[i])

        else:
            temp[int((array[i] - min_ele) / rngeOfBuckets)].append(array[i])


# Sortowanie osobno kazdego kubelka
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    # Posortowane elementy wrzucamy do finalnej tablicy
    k = 0
    for elem in temp:
        if elem:
            for i in elem:
                array[k] = i
                k = k + 1


noOfBuckets = 10

dict1 = {}
for a in range(len(lista2)):
    dict1[lista3[a]] = lista2[a]


start = time.time()
quick_sort(lista2)
#final = quick_sort(lista2)
#print('Oceny po posortowaniu:')
#print("final)
end = time.time()
print("Czas sortowania szybkiego: ")
print(end - start)

start = time.time()
bucketSort(lista2, noOfBuckets)
#print("Po sortowaniu: ", lista2)
end = time.time()
print("Czas sortowania kubełkowego: ")
print(end - start)

start = time.time()
scalanie = merge_sort(lista2,0,len(lista2)-1)
end = time.time()
#print(scalanie)
print("Czas sortowania przez scalanie: ")
print(end - start)

# Obliczanie sredniej
average = sum(lista2) / len(lista2)
print('Wartość średnia wynosi:')
print(average)

# Obliczanie mediany
mediana = statistics.median(lista2)
print('Mediana wynosi:')
print(mediana)
