"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import controller
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- listar cronológicamente los artistas")
    print("3- listar cronológicamente las adquisiciones")
    print("4- clasificar las  obras de un artista por técnica")
    print("5- clasificar las obras por la nacionalidad de sus creadores ")
    print("6- transportar obras de un departamento")
    print("6- proponer una nueva exposición en el museo ")



def incatalogo():
    return controller.incatalogo()

def cargardatos(catalogo):
    controller.caragardatos(catalogo)

def ultimosartistas(catalogo):
    ulartistas = lt.subList(catalogo["artistas"], lt.size(catalogo["artistas"])- 3,3)
    
    return  ulartistas

def ultimasobras(catalogo):
    ulobras = lt.subList(catalogo["obras"], lt.size(catalogo["obras"])- 3,3)
    
    return  ulobras
catalogo = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo = incatalogo()
        cargardatos(catalogo)
        print("artistas cargados: "+ str(lt.size(catalogo["artistas"])))
        print("obras cargadas: "+ str(lt.size(catalogo["obras"])))
        print("ultimos 3 artistas " + str(ultimosartistas(catalogo))+ "\n\n\n ")
        print("ultimas 3 obras  " + str(ultimasobras(catalogo)) + "\n\n\n ")

    elif int(inputs[0]) == 2:
        print("listando cronológicamente los artistas.")

    elif int(inputs[0]) == 3:
        print("listando cronológicamente las adquisiciones")

    elif int(inputs[0]) == 4:
        print("clasificando las  obras de un artista por técnica")
    elif int(inputs[0]) == 5:
        print("clasificando las obras por la nacionalidad de sus creadores")
    elif int(inputs[0]) == 6:
        print("transportando obras de un departamento")
    elif int(inputs[0]) == 7:
        print("Cargando información de los archivos ....")

    else:
        sys.exit(0)
sys.exit(0)
