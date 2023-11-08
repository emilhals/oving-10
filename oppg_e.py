from main import lagre_data_til_liste
import matplotlib.pyplot as plt

def sum_av_tall_over_fem(liste):
  total = 0
  for tall in liste:
    if (tall >= 5):
      total += tall - 5
  return total

gyldige_aar = []
aar_sumtemp=[]
aar=[]

for year in lagre_data_til_liste():
    infodager = 0
    for day in year:
        infodager+=1
    if infodager > 299:
        gyldige_aar.append(year)
        aar.append(int(year[5].dato.split(".")[2]))
        
for year in gyldige_aar:
    sumtemp=[]
    for day in year:
        try:sumtemp.append(float(day.midddeltemperatur.replace(",",".")))
        except:sumtemp.append(0)
    aar_sumtemp.append(sum_av_tall_over_fem(sumtemp))
    
plt.plot(aar,aar_sumtemp)
plt.xlabel("år")
plt.ylabel("forventet plantevekst")