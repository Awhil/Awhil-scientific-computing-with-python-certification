import xml.etree.ElementTree as TE

def main():
  data = '''
  <person>
    <name>Awhil</name>
    <phone type="intl">
        +1 312 131 ****
    </phone>
    <email hide="yes"/>
  </person>
  '''
  tree = TE.fromstring(data)
  print("Name:",tree.find("name").text)
  print("Attr:",tree.find("email").get("hide"))
  

if __name__ == "__main__":
    main()