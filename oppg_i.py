from main import lagre_data_til_liste
import matplotlib.pyplot as plt
import math

def numberList(inlist):
    newlist = [inlist[x+1]-inlist[x] for x in range(0,len(inlist)-1)]
    return newlist

class snitt_maaned:
    def __init__(self,snitt,maaned,aar): 
        self.snitt = snitt
        self.maaned = maaned
        self.aar = aar

fullist = []
maanedsnittlist =[] #snitt for hver måned i hvert år
maaned = [1,2,3,4,5,6,7,8,9,10,11,12]
templist = []
feil = 0

for year in lagre_data_til_liste():
    maanedlist = []
    for a in range(0,12):maanedlist.append([])
    for day in year:
        try: 
            maanedlist[int(day.dato.split(".")[1])].append(float(day.midddeltemperatur.replace(",", ".")))
        except: feil+=1
    fullist.append(maanedlist)

for a in range(0,len(fullist)-1):
    for b in  range(0,12):
        try:
            maanedsnitt = sum(fullist[a][b])/len(fullist[a][b])
            maanedsnittlist.append(snitt_maaned(maanedsnitt,b,a+1980))
        except:feil+=1

for d in range(0,len(maanedsnittlist)-1):
    templist.append(maanedsnittlist[a].snitt)

#plt.plot()
plt.ylabel("gjennomsnittstemperatur")
plt.xlabel("jan-des")

print(f"{feil} feil")