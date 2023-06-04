import json
def main():
  data = '''
  [
    { "id":"001",
      "x": "2",
      "name" : "Awhil"
    } ,
    { "id":"009",
      "x":"7",
      "name":"Lalo"}
  ]'''
  
  info = json.loads(data)
  print("User count:", len(info))
  for item in info:
    print("Name:",item["name"])
    print("Id:",item["id"])
    print("Value:",item["x"])
    
if __name__ == "__main__":
    main()