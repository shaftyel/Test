from subprocess import Popen, PIPE

# Función que captura la salida del comando hostname y
# lo envía a un txt


def capturar_comando():
    proceso = Popen("hostname", shell=True, stdout=PIPE)

    comando = open("captura.txt", "wb")
    for listado in proceso.stdout.readlines():
        comando.write(listado)
    comando.close()

    proceso.stdout.close()

# Función que lee la salida almacenada en el txt,
# la almacena en una variable, la cual es utilizada
# en un string de comandos para cambiar el hostname


def leer_captura():
    # Solicitamos el ingreso del nuevo hostname
    hostname_new = input('Ingrese el nuevo hostname: ')
    # Buscamos el actual hostname y lo almacenamos en variable
    f = open('captura.txt', 'r')
    hostname_old = f.readlines(1)
    f.close()
    # se agregan ambas variables al comando wmic
    # para cambio de hostname
    proceso = Popen("wmic computersystem where caption='"+hostname_old[0].rstrip(
        '\n')+"' rename "+hostname_new, shell=True, stdout=PIPE)
    # Se almacena la salida del comando ejecutado
    comando = open("captura2.txt", "wb")
    for listado in proceso.stdout.readlines():
        comando.write(listado)
        print(listado)
    comando.close()

    proceso.stdout.close()


capturar_comando()

leer_captura()
