#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two paramentes (hours and rate)

def computepay (hours, rate):
  regularHours = 40
  if hours > regularHours:
    print("\nYou exceeded",regularHours,"hours")
    overtime = hours - regularHours
    pay = (regularHours + overtime * 1.5) * rate
  else:
    print("\nYou preferred to be happy, well done")
    pay = hours * rate
  print("Your pay is: $",pay)
  
def main():
  try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
  except:
    print("\nError, please enter numeric input")
    quit()
  computepay(hours, rate)

if __name__ == "__main__":
  main()