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
    catalogo["artistas"] = lt.newList("ARRAY_LIST",cmpfunction=compareartistas)
    catalogo["obras"] = lt.newList("ARRAY_LIST")
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
def compareartistas ( artista1 , artista2):
    return(int(artista1["BeginDate"])> int(artista2["BeginDate"]))

# Funciones de ordenamiento
def ordenarartistas(catalogo):
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
    return catalogo