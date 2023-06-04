#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked about 40 hours
def main():
  regularHours = 40
  hours = float(input("Enter hours: "))
  rate = float(input("Enter rate: "))
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