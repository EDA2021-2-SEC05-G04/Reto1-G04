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
"""

from typing import Callable, List
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
def catalogonuevo():
    catalogo = {"artistas" : None,
    "obras": None,
    "ides": None,
    "departamento" : None,
    "nep": None,
    "costototal" : None,
    "pesoneto": None}
    catalogo["artistas"] = lt.newList("ARRAY_LIST", comparenombres)
    catalogo["obras"] = lt.newList()
    catalogo["ConstiID"] = lt.newList("ARRAY_LIST",compararcid)
    catalogo["departamento"] = lt.newList("ARRAY_LIST", comparardepartamento)
    catalogo["nep"]  = lt.newList("ARRAY_LIST")
    catalogo["costototal"] = 0
    catalogo["pesoneto"] = 0
    return(catalogo)

# Funciones para agregar informacion al catalogo


def addobra(catalogo, obra):
    lt.addLast(catalogo["obras"],obra)
    ides = obra["ConstituentID"].split(", ")
    for id in ides:
        idx = id.strip("[]' ")
        addartist(catalogo,idx,obra)
    dep = obra["Department"]
    adddepartamento(catalogo,dep, obra)


def adddepartamento(catalogo,dep, departamento):
    cat = catalogo["departamento"]
    posicion = lt.isPresent(cat, dep)
    if posicion > 0:
        depa = lt.getElement(cat, posicion)
    else:
        depa = nuevodepa(dep)
        lt.addLast(cat, depa)
    lt.addLast(depa["obras"], departamento)


def nuevodepa(depa):
    reto= {
        "departamento" : None,
        "obras" : None
    }
    reto["departamento"] = depa
    reto["obras"] = lt.newList("ARRAY_LIST")
    return(reto)

def addartist(catalog, cid, obra):
    cat = catalog["ConstiID"]
    posicion = lt.isPresent(cat, cid)
    if posicion > 0:
        artista = lt.getElement(cat, posicion)
    else:
        artista = nuevoide(cid)
        lt.addLast(cat, artista)
    lt.addLast(artista["obras"], obra)


def nuevoide(coid):
     ide = {"cid": None,
    "obras": None}
     ide["cid"] = coid 
     ide["obras"] = lt.newList("ARRAY_LIST") 
     return(ide)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def comparardepartamento(departamento, obra):
    if (departamento == obra['departamento']):
        return 0
    elif (departamento > obra['departamento']):
        return 1
    return -1 
def compararcid(cid, listacid):
    if (cid in listacid["cid"]):
        return(0)    
    return(-1)

def addcid(catalogo, artista):
    lt.addLast(catalogo["artistas"], artista)
def compararci(artista1, artista2):
    return (artista1["ConstituentID"] < artista2["ConstituentID"] )
def comparenombres(nombre, artista):
    if (nombre == artista['DisplayName']):
        return 0
    elif (nombre > artista['DisplayName']):
        return 1
    return -1

def buscarconsti(catalogo, consti):
    cat = catalogo["ConstiID"]
    pos = lt.isPresent(cat, consti)
    if pos > 0:
        elemento = lt.getElement(cat, pos)
    a = elemento["obras"]
    return(a)

def buscarco(catalogo, nombre):
    catalogo = catalogo["artistas"]
    pos = lt.isPresent(catalogo, nombre)
    if pos > 0:
        autor = lt.getElement(catalogo, pos)
    return(autor["ConstituentID"])

def totaldetecnicas(catalogo):
    histo = {}
    mayor = 0
    select = None
    for i in lt.iterator(catalogo):
        if i["Medium"] in (histo):
            histo[i["Medium"]] += 1
        else:
            histo[i["Medium"]]  = 1
    for h in histo:
        if histo[h] > mayor:
            mayor = histo[h]
            select = h 
    return(histo, select)

def listadodeobras(catalogo, tecnica):
    new = lt.newList("ARRAY_LIST")
    for i in lt.iterator(catalogo):
        if i["Medium"] == tecnica:
            a = {"titulo": i["Title"], "Fecha": i["Date"], "Medio": i["Medium"], "Dimensiones": i["Dimensions"],}
            lt.addLast(new, a)
    return new

def artistaenci(catalogo):
    histo = {}
    cat = catalogo["ConstiID"]
    artistas = catalogo["artistas"]
    artistas = mg.sort(artistas,compararci)
    for i in lt.iterator(cat):
        ci = i["cid"] 
        buscar = buscarartista(artistas, ci )
        if buscar != None:
            elemento = lt.getElement(artistas, buscar)
            nacionalidad = elemento["Nationality"]
            numero = lt.size(i["obras"])
            if nacionalidad in histo:
                histo[nacionalidad]["numero"] += numero
                lt.addLast( histo[nacionalidad]["obras"],i["obras"])
            else:
                histo[nacionalidad]= {
                      "numero" : numero,
                      "obras"   : lt.newList()
                }
                lt.addLast( histo[nacionalidad]["obras"], i["obras"])
                
    return(histo)        

def buscartop(histograma):
    mayor = 0
    reto = {}
    principal = None
    for i in histograma:
        if histograma[i]["numero"]  > mayor:
            mayor = histograma[i]["numero"]
            principal = histograma[i]["obras"]

    for i in histograma:
        reto[i] = histograma[i]["numero"]
    return(principal, histograma, mayor, reto)

def buscardepa(catalogo, departamento):
    cata = catalogo["departamento"]
    pos = lt.isPresent(cata, departamento)
    if pos > 0:
        elemento = lt.getElement(cata, pos)
    ret = elemento["obras"] 
    return(ret)

def ordenarporfecha(obra1, obra2):
    return(obra1["fecha"] > obra2["fecha"])
def ordenarporcosto(obra1, obra2):
    return(obra1["costo"] > obra2["costo"])

def filtrar(catalogo):
    nl = lt.newList("ARRAY_LIST")
    catf = mg.sort(catalogo, ordenarporfecha)
    catc = mg.sort(catalogo, ordenarporcosto)
    for i in range(1, 6):
        a = lt.getElement(catf, i)
        lt.addLast(nl, a)
    for h in range(1,6):
        p = lt.getElement(catc, h)
        lt.addLast(nl, p)
    return(nl)

def buscarartista(catalogo, elemento):
    i = 1
    j = lt.size(catalogo)
    encontro = False
    posa = None
    while (i <= j and not encontro):
        mid = (i + j)  // 2
        if (elemento == lt.getElement(catalogo, mid)["ConstituentID"]):
            posa = mid
            encontro = True 
        elif( elemento > lt.getElement(catalogo, mid)["ConstituentID"]):
            i = mid + 1
        else:
            j  = mid - 1
    return(posa)

def costoporobra(cato, catalogo):
    dicc= {}
    pesoneto =0
    if (catalogo["Height (cm)"] != "" and catalogo["Width (cm)"] != ""):
        area = (float(catalogo["Height (cm)"]) / 100) * (float(catalogo["Width (cm)"])/ 100)
        costo = area * 72.00
    elif (catalogo["Height (cm)"] != "" and catalogo["Width (cm)"] != "" and catalogo["Length (cm)"] != ""  ):
        area = (float(catalogo["Height (cm)"]) / 100) * (float(catalogo["Width (cm)"])/ 100) * (float(catalogo["Length (cm)"])/ 100)
        costo = area * 72.00
    elif (catalogo["Weight (kg)"] != ""):
        area = (catalogo["Weight (kg)"] )
        costo = area * 72.00
        pesoneto += int(area)
    else:
        costo =  48.00
    dicc["Titulo"] = catalogo["Title"]
    dicc["Artista"] = catalogo["ConstituentID"]
    dicc["clasificacion"] = catalogo["Classification"]
    dicc["fecha"] = catalogo["Date"]
    dicc["Medio"] = catalogo["Medium"]
    dicc["Dimensiones"] = catalogo["Dimensions"]
    dicc["costo"] = costo
    cato["costototal"] += costo
    cato["peso"] = pesoneto
    lt.addLast(cato["nep"], dicc)

def ordenarartistas(catalogo, fi, fo):
    cat = mg.sort(catalogo["artistas"], compareartistas)
    f1  = busqueda(cat,fi, 0)
    f2 = busqueda(cat,fo, 1)
    n1 = primero(cat,f1, "BeginDate")
    n2 =ultimo(cat, f2,  "BeginDate")
    a  = lt.subList(cat, n1 , (n2 +1)  -n1)
    return a
def compareartistas(artista1 , artista2):
    return(int(artista1["BeginDate"])< int(artista2["BeginDate"]))
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
    print(posa)
    return(posa)
def ordenarobras(catalogo,fi, fo):
    cat = mg.sort(catalogo, compararporfecha)
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
    return(l)
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