#Schreiben Sie ein Pogramm, das nach Eingabe des Radius in einer funktion des Kreisumfang berechnet.
#Verwenden Sie dazu die Konstante pi aus dem math-Paket

#Die Eingabe soll ein einer Funktion erfolgen, in der sichergestellt wird, dass es sich dabei
#  a) jedenfalls um eine Zahl
# und
#  b) eine positive Zahl handelt.

import math

def eingabe():
    correct = False
    while correct == False:
        r_str = input("Radius:")
        try:
            r = float(r_str)
            if r > 0:
                correct = True
            else:
                print("keine gültige Eingabe (r <= 0)")
        except ValueError:
                print("keine gültige Eingabe (keine Zahl)")
    return r
    
def kreisumfang(radius):
    umfang = 2*radius*3.14159265
    return umfang

kreisradius = eingabe()
print("eingegebener Radius:",kreisradius)

umfang = kreisumfang(kreisradius)
print("Kreisumfang:",umfang)
