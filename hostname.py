from subprocess import Popen, PIPE


def capturar_comando():
    proceso = Popen("hostname", shell=True, stdout=PIPE)

    comando = open("captura.txt", "wb")
    for listado in proceso.stdout.readlines():
        comando.write(listado)
        print(listado)
    comando.close()

    proceso.stdout.close()


def leer_captura():
    hostname_new = input('Ingrese el nuevo hostname: ')
    f = open('captura.txt', 'r')
    hostname_old = f.read()
    proceso = Popen(
        "wmic computersystem where caption='"+hostname_old+"'rename "+hostname_new, shell=True, stdout=PIPE)

    comando = open("captura2.txt", "wb")
    for listado in proceso.stdout.readlines():
        comando.write(listado)
        print(listado)
    comando.close()

    proceso.stdout.close()
    f.close()


capturar_comando()

leer_captura()
