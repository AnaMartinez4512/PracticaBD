import socket, os
from threading import *

class Servidor( Thread ):

    def __init__( self ):
        Thread .__init__( self )

    def run ( self ):
        self.process()

    def bindFileSocket( self ):
        self.fileSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.fileSocket.bind(('',9091))
        self.fileSocket.listen(1)
        print ("Esperando conexion archivos")

    def acceptFileSocket( self ):
        self.fileConnection, self.fileAddr = self.fileSocket.accept()
        print ("Conectado archivos")

    def bindControlSocket( self ):
        self.controlSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.controlSocket.bind(('',9090))
        self.controlSocket.listen(1)
        print "Esperando conexion"

    def acceptControlSocket( self ):
        self.controlConnection, self.controlAddr = self.controlSocket.accept()
        print "Conectado"
        while 1:
            datos = self.controlConnection.recv(1024)
            if not datos: break
            if datos[0:4] == "SEND":
                self.fileName = datos[5:]
                print self.fileName
                break

                
    def transferencia( self ):
        ruta = "/home/anna/Recibir/"
        f = open(ruta+self.fileName,"wb")
        while 1:
            datos = self.fileConnection.recv(1024)
            if not datos: break
            f.write(datos)
        f.close()
	
    def subir( self ):
       os.popen("mysql --user=root --password=anamartinez45 empresa< /home/anna/Recibir/espaldo3.sql")
            
    def cerrar( self ):
        self.controlConnection.close()
        self.fileConnection.close()
        self.controlSocket.close()
        self.fileSocket.close()

    def process( self ):
        while 1:
            self.bindControlSocket()
            self.acceptControlSocket()
            self.bindFileSocket()
            self.acceptFileSocket()
            self.transferencia()
	    self.subir()
            self.cerrar()

servidor = Servidor()
servidor.start()








    
