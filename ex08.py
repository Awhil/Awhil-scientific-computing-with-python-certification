#Write a program to read through a file and print the third word of lines that beginning with "From". file link: https://www.py4e.com/code3/mbox-short.txt
def main():
  try:
    with open ("mbox-short.txt","r") as file:
      lines = file.readlines()
      for line in lines:
        line = line.rstrip()
        words = line.split()
        #guardian in a compound statement
        if len(words)<3 or words[0] != "From":
          continue
        print(words[2])
  except:
    print("File not found")
  
if __name__ == "__main__":
  main()