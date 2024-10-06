from subprocess import check_output
import subprocess 
import platform


def detectar_os():
    #Detectar el sistema operativo
    sistema_os = platform.system()

    if sistema_os == 'Windows':
        print("Es sistema Windows")
         ##Este script funciona solo en windows ya que SYSTEMINFO es solo de windows 
        sistema = check_output('systeminfo',stderr = subprocess.STDOUT).decode('UTF-8')
        return sistema

    elif sistema_os in ['Linux','Darwin']: #Darwin es para MacOs
        print("Es sistema Unix")
         ##Para sistemas con base unix usaremos el siguiente codigo
        sistema = check_output(['uname', '-a'], stderr=subprocess.STDOUT).decode('UTF-8')
        return sistema
    else:
        return "Sistema no reconocido"
        
try:
    
    sistem_info = detectar_os()

    if sistem_info:
        registro = open('registro.txt','w+')
        registro.write(sistem_info)
        print("Confirmacion de informacion sustraida")
        registro.close()


except Exception as e:
    print("Ocurrio un error, no se reconoce el sistema operativo",e)


