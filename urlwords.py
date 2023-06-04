import urllib.request, urllib.parse, urllib.error
def main():
  #Abrimos una conexión con la UR para extraer el archivo
  fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
  counts = dict()
  for line in fhand:
      #Decodifica la línea de bytes a una cadena de caracteres 
      words = line.decode().split()
      for word in words:
          #Guardamos las palabras en el diccionario
          counts[word]= counts.get(word,0) + 1
  print(counts)
  
if __name__ == "__main__":
  main()