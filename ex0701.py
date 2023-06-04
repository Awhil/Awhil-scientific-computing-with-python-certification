#Write a program to read through a file and print the contents of the file (line by line) all in upper case. file link: https://www.py4e.com/code3/mbox-short.txt
def main():
  try:
    with open ("mbox-short.txt","r") as file:
      lines = file.readlines()
      for line in lines:
        line = line.rstrip()
        print(line.upper())
  except:
    print("File not found")
  
if __name__ == "__main__":
  main()