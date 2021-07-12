

import colorama
import git

print("\033[1;33m"+"""
d    d d s.     sSSs. d     S sss sssss   sSSSs     sSSSs   d        sss. 
S    S S  ~O   S      S    P      S      S     S   S     S  S      d      
S    S S   `b S       Ssss'       S     S       S S       S S      Y      
S sSSS S sSSO S       S   s       S     S       S S       S S        ss.  
S    S S    O S       S    b      S     S       S S       S S           b 
S    S S    O  S      S     b     S      S     S   S     S  S           P 
P    P P    P   "sss' P     P     P       "sss"     "sss"   P sSSs ` ss
"""+'\033[0;m')
print("\033[;36m"+"<======================================================>")
print("\033[;36m"+"Bienvenido a Hack-Tools\n Credor: @TheRootRobot")
print("\033[;36m"+"<======================================================>")
print("\033[4;35m"+"[1]Wireless\n[2]Herramientas de explotacion\n[3]SPAM\n[4]Sobre el creador")
print("\033[;36m"+"<======================================================>")
x = int(input("==> "))
if x==1:
	print("[+]Ataques Wireless[+]")
	print("[1]Wifite\n[2]Cerrar")
	print("Por ahora solo esta disponible wifite")
	a = int(input("==>"))
	#poniendo las funciones de la variable a
	if a==1:
		print("Iniciando instalacion wifite")
		print("Instalando wifite")
		git.Git("/home").clone("https://github.com/derv82/wifite")
		print("Instalacion completada!!!")
		print("Guardado en /home/Wifite/")
	if a==2:
		print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
	else:
	      print("Error fatal!!!!")
	      print("Intente denuevo")	


	print("Fin del programa")	
if x==2:
	print(chr(27)+"[1;33m"+"[+]Herramientas de Explotacion[+]")
	print("\033[4;35m"+"[1]Sqlmap\n[2]SET") 
	#poniendo funciones de la variable b 
	b = int(input("==> "))
	if b==1:
	    print("Iniciando instalacion de Sqlmap") 
	    print("Instalando Sqlmap")
	    git.Git("/home").clone("https://github.com/sqlmapproject/sqlmap")
	    print("Intalacion completada")
	    print("Sqlmap guardado en /home")
	
	if b==2: 
    	 print("Intalando SET")
    	 git.Git("/home").clone("https://github.com/trustedsec/social-engineer-toolkit")
    	 print("Instalacion completada")
    	 print("SET guardado en /home")
         

if x==3: 
    print("\033[;36m"+"[+]Herramientas de SPAM")
    print("\033[1;33m"+"[1]SETSMS\n [2]TBomb"+'\033[0;m')
    #poniendo funciones de varieble c
    c = int(input("==>"))
    if c==1:
     	print("Intalando SETSMS")
     	git.Git("/home").clone("https://github.com/Darkmux/SETSMS")
     	print("Instalacion completada")
     	print("Cerrando programa")
    if c==2:
        print("Intalando TBomb")
        git.Git("/home").clone("https://github.com/TheSpeedX/TBomb")
        print("Intalacion comletada")
if x==3:
    print("creador:@TheRootRobot")
    print("\033[1;33m"+"Canal de youtube: https://youtube.com/chammel/UCz2LXAQAHo9hihXOiPCpdtA"+'\033[0;m') 

     	