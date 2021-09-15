
from datetime import date, timedelta
from datetime import datetime

a = "2001-11-12"
b = "2001-11-1"
a = datetime.strptime(a, "%Y-%m-%d")
b = datetime.strptime(b, "%Y-%m-%d")
if a > b:
    print(a + timedelta(1))


    if a == None:
        aencontrado = False
        while not aencontrado:
            if ((fi - datetime.timedelta(1)) < fo):
                fi = fi - timedelta(1)
                a = busquedafechas(cat, fi)
            if a != None:
                aencontrado = True
    if b == None:
        bencontrado = False
        while not bencontrado:
            if ((fo + datetime.timedelta(1)) < fi):
                fo = fo - timedelta(1)
                b = busquedafechas(cat, fo)
            if b != None:
                bencontrado = True
datetime.strptime(lt.getElement(catalogo,mid)["DateAcquired"], "%Y-%m-%d")