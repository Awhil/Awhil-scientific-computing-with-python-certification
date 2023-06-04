#write a program which repeatedliy reads numbers until the user enters 'done'. Once 'done' is entered, print out the total, count and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number
def main():
  counter = 0
  total = 0.0
  while True:
    number = input("Enter a number: ")
    if number == "done":
      break
    try:
      number = float(number)
    except:
      print("Invalid input, try again")
      continue
    counter += 1
    total += number
  print("Total: ",total)
  print("Amount of numbers entered: ",counter)
  print("Average: ",total/counter)
    
if __name__ == "__main__":
  main()