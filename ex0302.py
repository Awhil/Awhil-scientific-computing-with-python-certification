#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 
def main():
  regularHours = 40
  try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
  except:
    print("\nError, please enter numeric input")
    quit()
  if hours > regularHours:
    print("\nYou exceeded",regularHours,"hours")
    overtime = hours - regularHours
    pay = (regularHours + overtime * 1.5) * rate
  else:
    print("\nYou preferred to be happy, well done")
    pay = hours * rate
  print("Your pay is: $",pay)
    
if __name__ == "__main__":
  main()