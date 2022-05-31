#Schreiben Sie ein Pogramm, das auf 2 möglichen Versionen, die in der Liste aufgeführten Personen begrüßt
#z.B.: "Hallo Peter!"
#
#Version 1: for-Schleife im Hauptpogramm, Ausgabe der Begrüßung in einem Unterpogramm

#Verion 2: for-Schleife und Ausgabe der Begrüßung in einem Unterpogramm

name = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung(name):
    print("Hallo",name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Pogramm!")
    
def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Hallo",ein_name)
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Pogramm!")
        
print("Version 1")
for name in name:
    begruessung(name)
    
print("Version 2")
begruessung(name)