import os
import subprocess
from os import system, name
try:
    from playsound import playsound
except:
    system('pip3 install playsound')
    from playsound import playsound
    


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class re:
    pare1 = color.YELLOW + "[" + color.END 
    pare2 = color.YELLOW + "]" + color.END 
    preg = color.GREEN + color.BOLD + "?" + color.END
    inf = color.PURPLE + color.BOLD + "Info:" + color.END
    nota = color.YELLOW + color.BOLD + "Nota:" + color.END
    err = color.RED + "Error:" + color.END
    fle = color.RED + color.BOLD + " --> " + color.END
    pare3 = color.BLUE + "(" + color.END 
    pare4 = color.BLUE + ")" + color.END 
    cic = color.CYAN + color.BOLD + " Ciclo " + color.END
    cics = color.CYAN + color.BOLD + " Ciclos " + color.END
    raya = color.RED + color.BOLD + " --> " + color.END
    web = color.YELLOW + color.BOLD
    pun = color.CYAN + color.BOLD + " : " + color.END
    on = color.GREEN + color.BOLD + color.UNDERLINE + "ONLINE" + color.END
    off = color.RED + color.BOLD + color.UNDERLINE + "OFFLINE" + color.END
    inic = color.PURPLE + color.BOLD + color.UNDERLINE + "HostChecker 3.0 ICMP-REQUEST".center(50) + color.END
    
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
def vari():
    global info, replicas, timeout, veces, tori    
    print(re.inic)
    print("") 
    playsound('audio/ini.mp3')      
    info = ""
    while True:    
        if info != "":            
            break
        else:                          
            info = input(re.pare1 + re.preg + re.pare2 + " Ingrese Web o Ip: [www.ejemplo.com]\n" + re.fle)
    
    while True:       
        replicas = input(re.pare1 + re.preg + re.pare2 + " Ingrese Nro. de consultas hantes de confirmar: Def. [3]\n" + re.fle)
        if replicas != "":     
            clear()   
            break    
        else:
            replicas = "3"
            print(color.GREEN + replicas + color.END)        
            break
         
    while True:    
        timeout = input(re.pare1 + re.preg + re.pare2 + " Set TimeOut : Def.[3]. Ej:[5]\n" + re.fle)
        if timeout != "":
            clear()
            break
        else:
            timeout = "3"
            print(color.GREEN + timeout + color.END)
            break
    
    while True:    
        veces = input(re.pare1 + re.preg + re.pare2 + " Ingrese Nro. de Ciclos que quiere ejecutar : Def. [20]. Ej:[3], ...[20], ...[100]\n" + re.fle)
        if veces != "":
            clear()
            break
        else:
            veces = "20" 
            print(color.GREEN +  veces + color.END)
            break
   
    clear()
    main(info,veces)

def ping_return_code(hostname):    
    ret_code = subprocess.call(['ping', '-c', replicas, '-W', timeout, hostname],
                               stdout=open(os.devnull, 'w'),
                               stderr=open(os.devnull, 'w'))
    return ret_code

def verify_hosts(host_list):
    global hostname, regresa    
    return_codes = dict()    
    for hostname in host_list:
        return_codes[hostname] = ping_return_code(hostname)         
        regresa = ping_return_code(hostname)
    return return_codes

def main(info,veces): 
    hosts_to_test = [info]    
    tiempo = int(replicas)*int(timeout)
    print("")
    print(re.inic)
    print("")
    print(re.pare1 + re.nota + re.pare2 + color.CYAN + color.BOLD + " Destino: " + color.END + color.YELLOW + str(info) + color.END)
    print(re.pare1 + re.nota + re.pare2 + color.CYAN + color.BOLD + " Ciclos totales: " + color.END + color.RED + color.BOLD + "[" + str(veces) + "]" + color.END)
    print(re.pare1 + re.nota + re.pare2 + color.CYAN + color.BOLD + " Numero de confirmaciones hantes de reporte: " + color.END + color.RED + color.BOLD + "[" + str(replicas) + "]" + color.END)
    print(re.pare1 + re.nota + re.pare2 + color.CYAN + color.BOLD + " Tiempo entre Chequeos: " + color.END + color.RED + color.BOLD + "[" + str(tiempo) + "]" + color.END + color.CYAN + color.BOLD + " Seg. Aprox." + color.END)
    print("")
    print(re.pare1 + re.nota + re.pare2 + color.RED + color.BOLD + color.UNDERLINE + " Si vez tu target ONLINE, y aqui lo vez OFFLINE." + color.END)
    print(re.pare1 + re.nota + re.pare2 + color.RED + color.BOLD + color.UNDERLINE + " El servidor esta usando IPV6." + color.END)
    print("")
    playsound('audio/pro.mp3')
    playsound('audio/ini2.mp3')
    x = 1
    while(x <= int(veces)):
        verify_hosts(hosts_to_test)     
        if x % 2 == 0: 
            amarelo = color.YELLOW + color.BOLD
        else:
            amarelo = color.RED + color.BOLD        
        if x & 1 == 1: 
            work = color.CYAN + color.BOLD
            work1 = " ...WORKING... ".center(60)
        else:
            work = color.GREEN + color.BOLD
            work1 = " ...WORKING... ".center(60)            
        if regresa == 1:            
            clear()
            print("")
            print(re.inic)
            playsound('audio/beep2.mp3')
            print("")
            print(re.pare1 + re.nota + re.pare2 + work + work1 + color.END)
            print(re.pare1 + re.inf + re.pare2 + re.cic + re.pare3 + amarelo + str(x) + color.END + re.pare4 + re.raya + re.web + hostname + color.END + re.pun + re.off)
            
        elif regresa == 0:            
            clear()
            print("")
            print(re.inic)
            playsound('audio/beep.mp3')
            print("")
            print(re.pare1 + re.nota + re.pare2 + work + work1 + color.END)
            print(re.pare1 + re.inf + re.pare2 + re.cic + re.pare3 + amarelo + str(x) + color.END + re.pare4 + re.raya + re.web + hostname + color.END + re.pun + re.on)
            
        else:
            clear()            
            print(re.pare1 + re.err + re.pare2 + " " + color.YELLOW + color.BOLD + hostname + color.END + color.RED + color.BOLD + " No Existe." + color.END)
            print("")                                            
            vari()            
        x = x + 1
        
    else:
        print("")
        print(color.CYAN + color.BOLD + "--------O-------".center(30) + color.END)
        print(re.pare1 + re.nota + re.pare2 + " " + color.RED + color.BOLD + "[" + veces + "]" + color.END + re.cics + re.fle + color.PURPLE + color.BOLD + color.UNDERLINE + "Clompletados." + color.END)
        print("")
        playsound('audio/fin.mp3')

error = ""
if __name__ == '__main__':  
    clear()      
    vari()
    
