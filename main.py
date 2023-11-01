import csv

def lagre_data_til_liste():
  with open('snoedybder_vaer_en_stasjon_dogn.csv', newline='') as file:
    hentet_data = csv.reader(file, delimiter=' ', quotechar=';')
    
    data = []
    
    for line in hentet_data:
      data.append(line)

    return data

def finn_snodager(liste):
  for linje in liste:
    print(linje)
  
  print(data)

if __name__ == "__main__":
  finn_snodager(lagre_data_til_liste())