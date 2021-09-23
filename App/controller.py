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
 """
import config as cf
from DISClib.ADT import list as lt
import model
import config as cf
import model
import csv

def initcatalogo():
    catalogo = model.catalogonuevo()
    return(catalogo)

def caragardatos(catalogo):
    cargarobras(catalogo)
    cargarartistas(catalogo)
    

def cargarobras(catalogo):
    obraarchivo = cf.data_dir +"Artworks-utf8-small.csv"
    archivo = csv.DictReader(open(obraarchivo, encoding="utf-8"))
    for obra in archivo:
        model.addobra(catalogo, obra)

def cargarartistas(catalogo):
    artistaarchivo = cf.data_dir + "Artists-utf8-small.csv"
    archivo = csv.DictReader(open(artistaarchivo, encoding="utf-8"))
    for artista in archivo:
        model.addcid(catalogo, artista)

def buscartop(histo):
   return (model.buscartop(histo))
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento


def ordenaraa(catalogo,fecha1, fecha2):
    a = model.ordenarartistas(catalogo,fecha1,fecha2)
    return a
def fechas(catalogo, f1,f2,tamano,ord):
    ord = model.ordenarobras(catalogo,f1,f2,tamano,ord)
    return(ord)

def buscarnombre(catalogo):
    b = model.totaldetecnicas(catalogo)
    return b
def catalogonombre(catalogo, nombre):
    nn = model.buscarco(catalogo,nombre)
    a = model.buscarconsti(catalogo,nn)
    return a
def infoobras(catalogo, tecnica):
    a = model.listadodeobras(catalogo, tecnica)
    return a
def nacionalidad(catalogo):
    return ( model.artistaenci(catalogo))

def buscardepa(catalogo, depa ):
    api = model.buscardepa(catalogo, depa )
    for i in lt.iterator(api): 
        model.costoporobra(catalogo, i)
def filtrar(catalogo):
    return ( model.filtrar(catalogo))
    
# Funciones de consulta sobre el catálogo
