from main import lagre_data_til_liste
import matplotlib.pyplot as plt
import math

gyldig_vind = []
vinddager = []
hoyvind = []
aar = []
feil = 0

for year in lagre_data_til_liste():
    infodager = 0
    for day in year:
        infodager+=1
    if infodager > 299:
        gyldig_vind.append([])
        for day in year:
            midvind = day.middelvind
            try:
                midvind = float(midvind.replace(",",".").replace("-",""))
                gyldig_vind[int(day.dato.split(".")[2])-1981].append(midvind)
            except:feil+=1

gyldig_vind.sort
for a in range(0,len(gyldig_vind)-1):
    lengde = len(gyldig_vind[a])
    hoyvind.append(gyldig_vind[a][lengde-1])
    if lengde%2==0:
        lengde = int(lengde/2)
        verdi1 = gyldig_vind[a][lengde]
        verdi2 = gyldig_vind[a][lengde-1]
        vinddager.append(verdi1/2+verdi2/2)
    else:
        lengde = int(lengde/2)
        verdi0 = gyldig_vind[a][math.floor(lengde)]
        vinddager.append(verdi0)
    aar.append(a+1981)
    
plt.plot(aar,vinddager,"r")
plt.plot(aar,hoyvind,"b")
plt.xlabel("år")
plt.ylabel("årlig nuddelvind b=max, r=median")
plt.show()