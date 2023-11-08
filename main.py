import csv, datetime
import matplotlib.pyplot as plt

class DagInfo:
  def __init__(self, navn, stasjon, dato, snødybde, nedbør, middeltemperatur, skydekke, middelvind):
    self.navn = navn
    self.stasjon = stasjon
    self.dato = dato
    self.snødybde = snødybde
    self.nedbør = nedbør
    self.middeltemperatur = middeltemperatur
    self.skydekke = skydekke
    self.middelvind = middelvind

def lagre_data_til_liste():
  dag_info_list = []
  
  with open('snoedybder_vaer_en_stasjon_dogn.csv', newline='') as file:
    hentet_data = csv.reader(file, delimiter=' ', quotechar=';')
    
    for line in hentet_data:
      for i in line:
        split_line = i.split(';')
      
        if split_line[0] == "Venabu":
          try:
            dag = DagInfo(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6], split_line[7])
            dag_info_list.append(dag)
          except:
            raise
            
    return dag_info_list

# Oppgave B
def beregn_antall_dager_med_skifore(dag_liste):
  skifore_per_vintersesong = {}
  
  for dag in dag_liste:
    if dag.snødybde != '-' and int(dag.snødybde) >= 20:
      dato = datetime.datetime.strptime(dag.dato, "%d.%m.%Y")
    
      if dato.month >= 10: 
        vintersesong = f"{dato.year}/{dato.year + 1}"
      else:
        vintersesong = f"{dato.year - 1}/{dato.year}"
       
      if vintersesong not in skifore_per_vintersesong:
        skifore_per_vintersesong[vintersesong] = 0
      
      skifore_per_vintersesong[vintersesong] += 1
    
  return skifore_per_vintersesong

# Oppgave C
def beregn_skifore_trend(x_akse, y_akse):  
  N = len(x_akse)-1

  x_akse = [int(aar.split('/')[0]) for aar in vinter_sesong.keys()]
  y_akse = list(y_akse)
  
  xAverage = sum(x_akse)/N
  yAverage = sum(y_akse)/N
    
  aTop = sum([((x_akse[i]-xAverage)*(y_akse[i]-yAverage)) for i in range(0,N)])
  aBot = sum([(x_akse[i]-xAverage)**2 for i in range(0,N)])
    
  a = aTop/aBot
  b = yAverage-a*xAverage
  
  return [a, b, x_akse, y_akse]
  
# Oppgave D
def snodybde_trend_plott(a, b, vintersesong):
  sesong_med_snodybde = {}
  
  for aar, dager in vintersesong.items():
    print(f"{aar}. dager: {dager}")
    if dager >= 200:
      sesong_med_snodybde[aar] = dager
      
  print(sesong_med_snodybde.keys())
  
  aar = [int(aar.split('/')[0]) for aar in sesong_med_snodybde.keys()]
  snodybder = list(sesong_med_snodybde.values())
  
  start_aar = min(aar)
  slutt_aar = max(aar)
  
  print(min(aar))
  
  y_start = a * start_aar + b
  y_slutt = a * slutt_aar + b
  
  plt.scatter(aar, snodybder, color='blue', label='Data')
  plt.text(aar[0], snodybder[0], f'{aar[0]}', ha='left')
  plt.text(aar[1], snodybder[1], f'{aar[1]}', ha='right')
  
  
  plt.plot(aar, snodybder, marker='o', label='Antall dager med skiføre')
  
  plt.plot([start_aar, slutt_aar], [y_start, y_slutt], color='red', label='Trend')
  
  plt.xlabel('År')
  plt.ylabel('Antall dager med skiføre') 
  
  plt.title('Dager med snø per vintersesong')
  plt.legend()
  
  plt.show()

vinter_sesong = beregn_antall_dager_med_skifore(lagre_data_til_liste())

sesong = vinter_sesong.keys()
snodager = vinter_sesong.values()
a = beregn_skifore_trend(sesong, snodager)[0]
b = beregn_skifore_trend(sesong, snodager)[1]
x_akse = beregn_skifore_trend(sesong, snodager)[2]
y_akse = beregn_skifore_trend(sesong, snodager)[3]

snodybde_trend_plott(a, b, vinter_sesong)