import  socket, os

os.popen("mysqldump --user=root --password=anamartinez45 empresa > /home/anna/Enviar/respaldo.sql")
ruta = "C:\\enviar\\"
filename = "respaldo.sql"
HOST = "172.20.10.5"

CPORT = 9090
FPORT = 9091

control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
control.connect((HOST,CPORT))
control.send("SEND" + filename)
control.close()

archivo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
archivo.connect((HOST,FPORT))

f = open(ruta+filename,"rb")
datos = f.read()
f.close()

archivo.send(datos)
archivo.close()
