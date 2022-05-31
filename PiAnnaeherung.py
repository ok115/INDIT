intVariable = 0
floatPi = 0
summe = 0

strTerme = input('Anzahl der Terme eingeben:')
intTerme = int(strTerme)

while intVariable <= intTerme:
    
    floatPi = (((-1)**intVariable) / (2*intVariable +1))
    summe += floatPi
    intVariable += 1
    
print('Annaeherung von Pi beträgt:', summe*4)