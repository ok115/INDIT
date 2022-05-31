strWetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch':")

if strWetter.lower() == "sonnig" or strWetter.lower() == "sonne":
    print("Gardenparty")
elif strWetter.lower() == "regnerisch" or strWetter.lower() == "regen":
    print("Kellerparty")
else:
    print("bitte entweder 'sonnig oder 'regnerisch 'eingeben'!")
    
