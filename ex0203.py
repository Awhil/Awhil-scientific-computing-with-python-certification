#Excercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay 
def main():
  hours = input("Enter Hours: ")
  rate = input("Enter Rate: ")
  grossPay = float(hours) * float(rate)
  print("Gross Pay is: ",grossPay)
  
if __name__ == "__main__":
  main()