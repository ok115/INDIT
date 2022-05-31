#if (Bedingung):
#   Anweisung 1
#else:
#   Anweisung 2
strZahl1 = input("Eingabe 1. Zahl1 ")
floatZahl1 = float(strZahl1)
print(floatZahl1)

strZahl2 = input("Eingabe 2. Zahl2: ")
floatZahl2 = float(strZahl2)
print(floatZahl2)

#die kleinere Zahl soll von der größeren Zahl subtrahiert werden

if floatZahl1 > floatZahl2:
    floatDifferenz = floatZahl1 - floatZahl2
    floatNegDifferenz = floatZahl2 - floatZahl1
    print("Differenz: ", floatDifferenz)
    print("Differenz: ", floatNegDifferenz)
elif floatZahl2 > floatZahl1:
    floatDifferenz = floatZahl2 - floatZahl1
    floatNegDifferenz = floatZahl1 - floatZahl2
    print("Differenz: ", floatDifferenz)
    print("Differenz: ", floatNegDifferenz)
else:
    print("Differenz wäre 0")
    
       
