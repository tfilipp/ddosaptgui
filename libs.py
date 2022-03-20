import os
import config
from colorama import Fore,init

init(autoreset=True)

# clsX
def cls(clsX):
	if clsX:
		os.system("clear")

# detectOS
def detectOS():
	if os.path.exists('/usr/bin/pacman'):
		osX = 'arch'
	elif os.path.exists('/usr/bin/apt'):
		osX = 'debian'
	return osX

# commandGEN
def gencommand(osX,c,pkg):
	def qQ(osX,q,pkg):
		if pkg == 'none' or pkg == 'None':
			if osX == 'arch':
				return str(q['arch'])
			elif osX == 'debian':
				return str(q['debian'])
		else:	
			if osX == 'arch':
				return str(q['arch']) + str(pkg)
			elif osX == 'debian':
				return str(q['debian']) + str(pkg)


	if c == 'install':
		q = config.commands['install']
		return qQ(osX,q,pkg)
	elif c == 'update':
		q = config.commands['update']
		return qQ(osX,q,pkg)
	elif c == 'upgrade':
		q = config.commands['upgrade']
		return qQ(osX,q,pkg)
	elif c == 'remove':
		q = config.commands['remove']
		return qQ(osX,q,pkg)
	else:
		print('Нет комманды')
		exit()

# exit
def ext(clsX):
    cls(clsX)
    exit()

# install
def install(clsX,osD):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █ █▄ █ █▀ ▀█▀ ▄▀█ █   █     █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀
    █ █ ▀█ ▄█  █  █▀█ █▄▄ █▄▄   █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄
    """)
    print(" ")
    print(Fore.RED+"You might input your password if you have not already.")
    print(" ")
    ip=input("Package name>>>")
    q = gencommand(osD,'install',ip)
    os.system(q)
    cls(clsX)

# update
def update(clsX,osD):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █ █ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀   █▀█ █▀▀ █▀█ █▀█ █▀
    █▄█ █▀▀ █▄▀ █▀█  █  ██▄   █▀▄ ██▄ █▀▀ █▄█ ▄█
        """)
    print(" ")
    print(Fore.RED+"You might input your password if you have not already.")
    print(" ")
    		# os.system("sudo apt update && clear")
    os.system(gencommand(osD,'update','none'))
    cls(clsX)

# upgrade
def upgrade(clsX,osD):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █ █ █▀█ █▀▀ █▀█ ▄▀█ █▀▄ █▀▀   ▄▀█ █   █     █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀ █▀
    █▄█ █▀▀ █▄█ █▀▄ █▀█ █▄▀ ██▄   █▀█ █▄▄ █▄▄   █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄ ▄█
        """)
    print(" ")
    print(Fore.RED+"You might input your password if you have not already.")
    print(" ")
    os.system(gencommand(osD,'upgrade','None'))
    cls(clsX)

# about
def about(clsX):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    
         ▄▀█ █▄▄ █▀█ █ █ ▀█▀
         █▀█ █▄█ █▄█ █▄█  █ 
    """)
    print("""
        ddOS apt GUI v 0.0.1
        Created by ddosTEAM
    """)

# change os
def chos(clsX,osD):
    cls(clsX)
    osss = osD
    if osD == 'arch':
        osD = 'debian'
    elif osD == 'debian':
        osD = 'arch'
    print(f"Current os: {osss} --> {osD}")
    return osD

# clear terminal
def clsXc(clsX):
    cls(clsX)
    clssss = clsX
    if clsX:
        if True:
            clsX = False
    else:
        if True:
            clsX = True
    print(f"Enable cls() is: {clssss} --> {clsX}")
    return clsX