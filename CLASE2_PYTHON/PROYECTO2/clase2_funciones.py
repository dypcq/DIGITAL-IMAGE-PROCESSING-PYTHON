import time
#abrir un archivo de texto en modo lectura
archivo=open("C:\\Users\\pdsjo\\Desktop\\datos_sensor.txt","r")
#uso del metodo read para leer el contenido del archivo de texto
temperatura=list()
humedad=[]
#acceder a cada linea del contenido del archivo de texto
print("IMPRIMIR CADA LINEA")
time.sleep(2)
for linea in archivo:
    #determinar cuantos elementos hay en cada linea
    Nl=len(linea)
    linea_n=linea[0:Nl-1]
    #crear lista_int
    lista_int=linea_n.split(",")
    print(lista_int)
    #acceder a cada posición y almacenarlo en su respectiva lista
    #almacenar la temperatura en la lista temperatura
    temperatura.append(lista_int[0])
    #almacenar la humedad en la lista humedad
    humedad.append(lista_int[1])
    time.sleep(3)

#cerrar el recurso del manejo de archivo de texto
archivo.close()
print(temperatura)
print(humedad)