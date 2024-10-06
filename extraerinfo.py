from subprocess import check_output
import subprocess 

sistema = check_output('systeminfo',stderr = subprocess.STDOUT)

registro = open('resgistro.txt','w+')
registro.write(sistema)
print("Confirmacion de informacion sustraida")
registro.close()

