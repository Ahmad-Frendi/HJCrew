import socket

def portscan():
  host=raw_input("HOST :>   ")
  rem=socket.gethostbyname(host)
  try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if s==1:
      print "{}  :OPEN!".format(s)
    s.close()
  except:
    print "GAGAL!"
