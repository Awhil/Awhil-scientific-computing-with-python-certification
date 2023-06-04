#Write a program to read through a file and keep a word count in a dictionary, also find the most  common word. file link: https://www.py4e.com/code3/intro.txt and https://www.py4e.com/code3/clown.txt
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
    print(dictionary)

    #now we want to find the most common word
    largest_value = -1
    theword = None
    for key,value in dictionary.items():
      #capture/remember the word that was largest
      if largest_value == -1 or value > largest_value:
        largest_value = value
        theword = key
    print("The most common word is '",theword,"':",largest_value)
  except:
    print("File not found")
  
if __name__ == "__main__":
  main()