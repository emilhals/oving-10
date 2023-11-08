from main import lagre_data_til_liste
import matplotlib.pyplot as plt

def sammenhengende_nuller(liste):
    antall_nuller = 0
    lengste_antall = 0
    for nummer in liste:
        if nummer == 0:
            antall_nuller += 1
        else:
            if lengste_antall < antall_nuller:
                lengste_antall = antall_nuller
            antall_nuller = 0
    return lengste_antall

gyldige_aar_nedbør = []
lengste_torke = []
aar = []

for year in lagre_data_til_liste():
    infodager = 0
    for day in year:
        infodager+=1
    if infodager > 299:
        gyldige_aar_nedbør.append([])
        for day in year:
            nedbor = day.nedbør
            try:nedbor = float(nedbor.replace(",",".").replace("-",""))
            except:nedbor = 0
            gyldige_aar_nedbør[int(day.dato.split(".")[2])-1981].append(nedbor)

for a in range(0,len(gyldige_aar_nedbør)-1):
    lengste_torke.append(sammenhengende_nuller(gyldige_aar_nedbør[a]))
    aar.append(a+1981)
    
plt.plot(aar,lengste_torke)
plt.xlabel("år")
plt.ylabel("lengste tørke")
plt.show()