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

gyldige_aar_pendag = []
antall_pendager = []
aar = []

for year in lagre_data_til_liste():
    infodager = 0
    for day in year:
        infodager+=1
    if infodager > 299:
        gyldige_aar_pendag.append([])
        for day in year:
            pendag = day.skydekke
            try:pendag = float(pendag.replace(",",".").replace("-",""))
            except:pendag = 4
            if pendag <= 3:
                gyldige_aar_pendag[int(day.dato.split(".")[2])-1981].append(pendag)

for a in range(0,len(gyldige_aar_pendag)-1):
    antall_pendager.append([])
    antall_pendager[a] = sum(gyldige_aar_pendag[a])
    aar.append(a+1981)
    
plt.plot(aar,antall_pendager)
plt.xlabel("år")
plt.ylabel("antall pendager")
plt.show()