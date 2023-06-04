import socket
def main():
  #se indica que se utilizará IPv4 para la comunicación y se especifica que se utilizará el protocolo de transporte TCP
  mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  #Se establece una conexión con el servidor en la dirección 'data.pr4e.org' y el puerto 80 
  mysock.connect(('data.pr4e.org', 80))
  #Se crea una cadena de solicitud HTTP GET para obtener el archivo romeo.txt del servidor y codifica.
  cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
  #Enviamos la solicitud HTTP al servidor 
  mysock.send(cmd)

  while True:
      #Se puede recibir hasta 512 bytes de datos del servidor
      data = mysock.recv(512)
      #Si no hay mas datos que recibir sale del ciclo
      if(len(data)<1):
          break
      #Imprimimos los datos recibidos decodificados en formato de cadena
      print(data.decode())
  mysock.close
  
if __name__ == "__main__":
  main()