#str = "X-DSPAM-Confidence: 0.8475 "
#use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number
def main():
  str = "X-DSPAM-Confidence: 0.8475 "
  str = str.rstrip()
  space_position = str.find(" ")
  number = str[space_position:]
  value = float(number)
  print(value)
  
if __name__ == "__main__":
  main()