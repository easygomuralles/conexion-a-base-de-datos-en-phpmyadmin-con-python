import pymysql

miConexion = pymysql.connect(host='localhost',user='root',passwd='',db='inicio')
cur=miConexion.cursor()
cur.execute("select nombre , email from cuentas" )
for nombre,email in cur.fetchall():
    print(nombre,"",email)

miConexion.close()
    

#EXPLICACION DEL COD

#import pymysql                                                                       IMPORTAR LA LIBRERIA PARA PODER IR A TRAER DATOS
#
#miConexion = pymysql.connect(host='localhost',user='root',passwd='',db='inicio')      CONECTAR A EL SERVIDOR CON LAS CREDENCIALES 
#cur=miConexion.cursor()                                                               DEFINIR LA CONEXION
#cur.execute("select nombre , email from cuentas" )                                    SELECCIONAR PARAMETROS DE QUE TABALA Y QUE PARAMETROS QUEREMOS IR A TRAER
#for nombre,email in cur.fetchall():                                                   DEFINIR LOS CAMPOS QUE SE VAN A IR A TRAER
#    print(nombre,"",email)                                                            MOSTRAR EN CONSOLA O PANTALLA LOS DATOS CON PRINT
 
#miConexion.close()                                                                    CERRAR LA CONEXION
