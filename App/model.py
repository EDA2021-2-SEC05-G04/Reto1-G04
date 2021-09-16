"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ix
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as mg
from datetime import date, timedelta 
from datetime import datetime
from time import process_time 
assert cf
import sys
sys.setrecursionlimit(10**6)



"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def catalogonuevo(tipo):
    catalogo = {"artistas" : None,
    "obras": None}
    if tipo == 1:
        catalogo["artistas"] = lt.newList("ARRAY_LIST", cmpfunction=compareartistas)
        catalogo["obras"] = lt.newList("ARRAY_LIST", cmpfunction=compararporfecha)
    elif tipo == 2:
        catalogo["artistas"] = lt.newList("SINGLE_LINKED", cmpfunction=compareartistas)
        catalogo["obras"] = lt.newList("SINGLE_LINKED", cmpfunction=compararporfecha)
    return catalogo

# Funciones para agregar informacion al catalogo
def agregararobra(catalogo, obra):
    lt.addLast(catalogo["obras"], obra)
    return catalogo
    
def agregarartista(catalogo, artista):
    lt.addLast(catalogo["artistas"], artista)
    return catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareartistas(artista1 , artista2):
    return(artista1["BeginDate"] > artista2["BeginDate"])
def compararporfecha(obra1, obra2):

    if obra1["DateAcquired"] == "":
        ret = False
    elif obra2["DateAcquired"] == "":
        ret = True
    else:
        fecha1 = datetime.strptime(obra1["DateAcquired"], "%Y-%m-%d")
        fecha2 = datetime.strptime(obra2["DateAcquired"], "%Y-%m-%d")
        ret = fecha1 > fecha2
    return(ret)
def primero(catalogo, pos, str):
    primero = False
    aux = pos
    elemento = lt.getElement(catalogo, pos)[str]
    while not primero:
        if lt.getElement(catalogo, aux-1)[str] == elemento:
            #print( str(lt.getElement(catalogo, aux)["DisplayName"]))
            aux -= 1
        else:
            return(aux)
def ultimo(catalogo, pos,str):
    primero = False
    aux = pos
    elemento = lt.getElement(catalogo, pos)[str]
    while not primero:
        if lt.getElement(catalogo, aux+1)[str] == elemento:
            aux += 1
        else:
            return(aux)
# Funciones de ordenamiento
def busqueda(catalogo, n, inicio):
    i = 1
    j = lt.size(catalogo)
    encontro = False
    posa = None
    while (i <= j and not encontro):
        mid = (i + j)  // 2
        if (n == int(lt.getElement(catalogo, mid)["BeginDate"])):
            posa = mid
            encontro = True 
        elif( n  > int(lt.getElement(catalogo, mid)["BeginDate"])):
            i = mid + 1
        else:
            j  = mid - 1
    if posa == None:
        if inicio == 0:
            posa = busqueda(catalogo, n +1,0)
        else:
            posa = busqueda(catalogo, n -1,1)

    return(posa)
def ordenarartistas(catalogo, fi, fo):

    tamano  = lt.size(catalogo)
    h = 1
    while h < tamano//3: 
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, tamano):
            j = i
            while (j >= h) and compareartistas(lt.getElement(catalogo, j-h+1) , lt.getElement(catalogo, j+1)):
                lt.exchange(catalogo, j+1, j-h+1)
                j -= h
        h //= 3  
    f1  = busqueda(catalogo,fi, 0)
    f2 = busqueda(catalogo,fo, 1)
    n1 = primero(catalogo,f1, "BeginDate")
    n2 =ultimo(catalogo, f2,  "BeginDate")
    a  = lt.subList(catalogo, n1 , (n2 +1)  -n1)
    return a
def busquedafechas(catalogo, n ):
    i = 1
    j = lt.size(catalogo)
    encontro = False
    posa = None
    while (i <= j and not encontro):
        mid = (i + j)  // 2
        if (n == datetime.strptime(lt.getElement(catalogo,mid)["DateAcquired"], "%Y-%m-%d")):
            posa = mid
            encontro = True 
        elif( datetime.strptime(lt.getElement(catalogo,mid)["DateAcquired"], "%Y-%m-%d") < n):
            j = mid - 1
        else:
            i  = mid + 1
    return(posa)
def eliminarvacias (catalogo):
    aux = lt.size(catalogo)
    primero = False
    while not primero:
        if lt.getElement(catalogo, aux-1)["DateAcquired"] == "":
            lt.removeLast(catalogo)
            aux -= 1
        else:
            primero = True 
    lt.removeLast(catalogo)
    return (catalogo)
def ordenarobras(catalogo,fi, fo, tamano, ord):
    start_time = process_time()
    if tamano < lt.size(catalogo):
         catalogo = lt.subList(catalogo, 1, tamano)
    else: 
        print("error")
    if ord == "mg":
        cat = mg.sort(catalogo, compararporfecha)
    elif ord == "is":
        cat = ix.sort(catalogo, compararporfecha)
    elif ord == "so":
        cat = sa.sort(catalogo, compararporfecha)
    elif ord == "qs":
        cat = qs.sort(catalogo, compararporfecha)
    else:
        print("error")
    stop_time = process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    cato = eliminarvacias(cat)
    print(cato)
    a = busquedafechas(cato, fi)
    b = busquedafechas(cato, fo) 
    print(a)
    print(b)
    res = (a+1) - b
    print(res)
    l = lt.subList(cato, a, res)
    print(lt.size(l))
    return(l, elapsed_time_mseg)
