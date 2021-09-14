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
assert cf




"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def catalogonuevo( ):
    catalogo = {"artistas" : None,
    "obras": None}
    catalogo["artistas"] = lt.newList("ARRAY_LIST", cmpfunction=compareartistas)
    catalogo["obras"] = lt.newList("ARRAY_LIST", cmpfunction=compareartistas)
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

def primero(catalogo, pos):
    primero = False
    aux = pos
    elemento = lt.getElement(catalogo, pos)["BeginDate"]
    while not primero:
        if lt.getElement(catalogo, aux-1)["BeginDate"] == elemento:
            #print( str(lt.getElement(catalogo, aux)["DisplayName"]))
            aux -= 1
        else:
            return(aux)
def ultimo(catalogo, pos):
    primero = False
    aux = pos
    elemento = lt.getElement(catalogo, pos)["BeginDate"]
    while not primero:
        if lt.getElement(catalogo, aux+1)["BeginDate"] == elemento:
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
            posa = busqueda(catalogo, n +1)
        else:
            posa = busqueda(catalogo, n -1)

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
    n1 = primero(catalogo,f1)
    n2 =ultimo(catalogo, f2)
    a  = lt.subList(catalogo, n1 , (n2 +1)  -n1)
    return a
