from main import lagre_data_til_liste
import matplotlib.pyplot as plt

def numberList(inlist):
    newlist = [inlist[x+1]-inlist[x] for x in range(0,len(inlist)-1)]
    newlist.append(0)
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
tomlist = []
aarsnitt = []
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
    templist.append(maanedsnittlist[d].snitt)
    tomlist.append(d)
for e in range(0,len(fullist)):
    a = 0
    for f in range(0,12):
        try:a+=sum(fullist[e][f])
        except:a+=0
    aarsnitt.append(a)

maaneddifflist = numberList(templist)
aar = [1980+a for a in range(0,len(lagre_data_til_liste()))]
aardiff = numberList(aarsnitt)

figure, axis = plt.subplots(2,2)
axis[0,0].plot(tomlist,templist,"b")
axis[1,0].plot(tomlist,maaneddifflist,"r")
axis[0,1].plot(aar,aarsnitt,"b")
axis[1,1].plot(aar,aardiff,"r")
plt.show()

print(f"{feil} feil")
