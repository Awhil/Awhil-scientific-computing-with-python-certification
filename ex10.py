#Write a program to read through a file and find the five most common words. file link: https://www.py4e.com/code3/intro.txt and https://www.py4e.com/code3/clown.txt
def main():
  dictionary = dict()
  name_file = input("Enter File: ")
  try:
    with open (name_file,"r") as file:
      lines = file.readlines()
      for line in lines:
        line = line.rstrip()
        words = line.split()
        for word in words:
          #update counter and add the new values
          dictionary[word] = dictionary.get(word,0) + 1
    #print(dictionary)

    #now we want to find the five most common words
    words = list()
    for key,value in dictionary.items():
      new_tuple = (value,key)
      words.append(new_tuple)

    words = sorted(words, reverse=True)

    for value,key in words[:5] :
      print(key,value)
  
  except:
    print("File not found")
  
if __name__ == "__main__":
  main()