import json
def main():
  data = '''
  {
    "name": "Awhil",
    "phone": {
        "type": "intl",
        "number": "+1 312 131 ****"
    },
    "email": {
        "hide": "yes"
    }
  }
  '''
  info = json.loads(data)
  print("Name:",info["name"])
  print("Hide:",info["email"]["hide"])
    
if __name__ == "__main__":
    main()