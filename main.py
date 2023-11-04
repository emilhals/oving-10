import csv, datetime

class DagInfo:
  def __init__(self, navn, stasjon, dato, snøbygde, nedbør, middeltemperatur, skydekke, middelvind):
    self.navn = navn
    self.stasjon = stasjon
    self.dato = dato
    self.snøbygde = snøbygde
    self.nedbør = nedbør
    self.midddeltemperatur = middeltemperatur
    self.skydekke = skydekke
    self.middelvind = middelvind

def lagre_data_til_liste():
  dag_info_list = [0]
  
  with open('snoedybder_vaer_en_stasjon_dogn.csv', newline='') as file:
    hentet_data = csv.reader(file, delimiter=' ', quotechar=';')
    
    for line in hentet_data:
      #print(line)
      for i in line:
        split_line = i.split(';')
      
        if split_line[0] == "Venabu":
          try:
            dag = DagInfo(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6], split_line[7])
            dag_info_list.append(dag)
          except:
            raise 
  return dag_info_list


  
if __name__ == "__main__":  
  print('')