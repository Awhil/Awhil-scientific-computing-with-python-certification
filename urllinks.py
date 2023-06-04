#link: http://www.py4e.com/code3/bs4.zip
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

def main():
    #Ingore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input("Enter- ")
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    #Retrive all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get("href",None))
    
if __name__ == "__main__":
    main()