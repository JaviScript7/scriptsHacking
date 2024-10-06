import nmap
import socket
import netifaces

#print("      _             _ ____            _       _   ")
#print("     | | __ ___   _(_) ___|  ___ _ __(_)_ __ | |_ ")
#print("  _  | |/ _` \ \ / / \___ \ / __| '__| | '_ \| __|")
#print(" | |_| | (_| |\ V /| |___) | (__| |  | | |_) | |_ ")
#print("  \___/ \__,_| \_/ |_|____/ \___|_|  |_| .__/ \__|")
#print("                                       |_|        ")
#print("Ip de los equipos conectados a la red")

def myip():
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8",80))
   #ip = ip.getsockname()[0]
    return ip.getsockname()[0]


gtw = netifaces.gateways()
ip_gtw = gtw['default'][netifaces.AF_INET][0] + '/24'

def scaner():
    nm = nmap.PortScanner()

    nm.scan(hosts=ip_gtw,arguments='-n -sP -PE -PA21,23,80,3389')
    host_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]

    archivo = open('scan.txt','w')
    for host,status in host_list:
        print(host,status)
        if host == myip():
            print(host,status,"<--Tu dispositivo")
        archivo.write(host+'\n')
    archivo.close()

print("__________________________\n")
print("IP del equipo: ",myip())
print("IP del Gateway: ",ip_gtw)
print("IP de los equipos conectados:")
scaner()