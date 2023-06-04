import xml.etree.ElementTree as TE

def main():
  input = '''
  <stuff>
      <users>
          <user x="3">
              <id>001</id>
              <name>Awhil</name>
          </user>
          <user x="7">
              <id>009</id>
              <name>Kathy</name>
          </user>
      </users>
  </stuff>'''

  stuff = TE.fromstring(input)
  lst = stuff.findall('users/user')
  print('User count:', len(lst))

  for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

if __name__ == "__main__":
    main()