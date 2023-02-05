
from mysql.connector import Error

import mysql.connector

class DAO():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='hotel_WC'
            )
        except Error as ex :
            print("Error al intentar la coneccion:{0}".format(ex))
            
#-------------------------------------------------------------------------------------------------
            
    def listarTarifas(self):
         if self.conexion.is_connected():
             try:
                 cursor= self.conexion.cursor()
                 cursor.execute("SELECT * FROM reservas")
                 resultados= cursor.fetchall()
                 return resultados
             except Error as ex :
                 print("Error al intentar la coneccion".format(ex))
                 
                 
#-----------------------------------------------------------------------------------------------
                 
    def registrarTarifa(self, datos):
        if self.conexion.is_connected():
            try:
                descuento = 5/100*datos[4]
                total= datos[4]-descuento
                 
                cursor = self.conexion.cursor()
                sql = "INSERT INTO reservas (id, nombre_completo, tipo_tarifa,dias, precio,total_precio) VALUES (DEFAULT,'{0}', '{1}', {2}, {3}, {4})"
                cursor.execute(sql.format(datos[0], datos[1], datos[2],datos[3],total))
                self.conexion.commit()
                print("******  ¡LA SOLICITUD FUE EXITOSA!  *******\n")
                print("precio de la habitacion$",datos[3],"\n")
                print("total a pagar $",datos[4],"\n")
                print("total a pagar con descuento aplicado",total,"\n")
                print("******  GRACIAS  *******\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
                
                


#-------------------------------------------------------------------------------------------------
    
    
    
    
    def actualizarTarifa(self, datos):
        if self.conexion.is_connected():
            try:
                descuento = 5/100*datos[5]
                total= datos[5]-descuento
                
                cursor = self.conexion.cursor()
                sql = "UPDATE reservas SET nombre_completo = '{1}',tipo_tarifa = '{2}', dias ={3}, precio = {4}, total_precio = {5} WHERE id = '{0}'"
                cursor.execute(sql.format(datos[0], datos[1], datos[2], datos[3], datos[4], total))
                self.conexion.commit()
                print("¡ACTUALIZACION EXITOSA!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
                
                
                
#------------------------------------------------------------------------------------------------



    def eliminarTarifa(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM reservas WHERE id = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡ELIMINACION EXITOSA!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
