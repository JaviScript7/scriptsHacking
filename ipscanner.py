import nmap 

'''
Script para obtener las direcciones Ip de la red LAN

nm = nmap.PortScanner()
host_scan = input("Ingresa tu Host: ")
while host_scan == " ":
    host_scan = input("Ingresa tu Host: ")
nm.scan(hosts = host_scan, arguments='-n -sP -PE -PA21,23,80,3389')
host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
archivo = open('scan.txt','w')
for hosts,status in host_list:
    print(hosts, status)
    archivo.write(hosts+'\n')
archivo.close()

'''
import os
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

nm = nmap.PortScanner()

nm.scan(hosts = "192.168.0.1/24", arguments='-sn')
host_list = [(x, nm[x]['addresses']['ipv4'],nm[x]['vendor']) for x in nm.all_hosts()]
for host,ip,vendor in host_list:
    if vendor:
        for i in vendor:
            a = vendor[i]
    else:
        a = "Not Found"

    host_name = nm[ip].hostname()

    if host_name == "":
        host_name = "Not Found"

    print(""" 
        {0}IP: {1}{2}
        {0}Hostname: {1}{3}
        {0}Vendor: {1}{4} 
        """.format(BLUE,RED,ip,host_name,a))
#for host,ip in host_list:
#    print("{0}IP: {1}{2} {0}Hostname: {1}{3} ".format(BLUE,RED,ip,nm[ip].hostname()))
