import os
import config
import distro
from colorama import Fore,init

init(autoreset=True)

# detectOS
def detectOS(lang,auto):
    spkg = []
    if os.path.exists('/usr/bin/apt'):
        osX = 'apt'
        spkg.append('apt')
    else:
        if os.path.exists('/usr/bin/pacman'):
            osX = 'pacman'
            spkg.append('pacman')
        if os.path.exists('/usr/bin/yay'):
            osX = 'yay'
            spkg.append('yay')
        if os.path.exists('/usr/bin/pamac'):
            osX = 'pamac'
            spkg.append('pamac')
    if spkg == []:
        return 'noos'
    if auto == False:
        print(f"{lang['spkg']}:")
        welcomecomprint(spkg)
        x = input(f"{lang['inputpkg']} :")
        osX = spkg[x-1]
    else:
        if 'apt' in spkg:
            osX = 'apt'
            return osX,distro.id(),spkg        
        if 'pacman' in spkg:
            osX = 'pacman'
        if 'yay' in spkg:
            osX = 'yay'
            return osX,distro.id(),spkg
        if 'pamac' in spkg:
            osX = 'pamac'  
    return osX,distro.id(),spkg

# clsX
def cls(clsX):
	if clsX:
		os.system("clear")

def welcomecomprint(list):
    for i in range(len(list)):
        print(f"{Fore.GREEN}[{i+1}] {Fore.YELLOW}{list[i]}")


# commandGEN
def gencommand(osX,c,pkg):
	def qQ(osX,q,pkg):
		if pkg == 'none' or pkg == 'None':
			if osX == 'yay':
				return str(q['yay'])
			elif osX == 'pamac':
				return str(q['pamac'])
			elif osX == 'pacman':
				return str(q['pacman'])
			elif osX == 'apt':
				return str(q['apt'])
		else: return str(q[osX]) + str(pkg)
            # if osX == 'yay':
            #     return str(q['yay']) + str(pkg)
            # elif osX == 'pamac':
            #     return str(q['pamac']) + str(pkg)
            # elif osX == 'pacman':
            #     return str(q['pacman']) + str(pkg)
            # elif osX == 'apt':
            #     return str(q['apt']) + str(pkg)	

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
def install(clsX,osD,lang):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █ █▄ █ █▀ ▀█▀ ▄▀█ █   █     █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀
    █ █ ▀█ ▄█  █  █▀█ █▄▄ █▄▄   █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄
    """)
    print(" ")
    print(Fore.RED+f"{lang['install']}")
    print(" ")
    ip=input(f"{lang['pkgname']}>>>")
    q = gencommand(osD,'install',ip)
    os.system(q)
    cls(clsX)

# delete
def deletee(clsX,osD,lang):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █▀█ █▀▀ █▄  ▄█ █▀█ ▀▄    ▄▀ █▀▀  █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀
    █▀▄ ██▄ █ ▀▀ █ █▄█   ▀▄▄▀   ██▄  █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄
    """)
    print(" ")
    print(Fore.RED+f"{lang['remove']}")
    print(" ")
    ip=input(f"{lang['pkgname']}>>>")
    q = gencommand(osD,'remove',ip)
    os.system(q)
    cls(clsX)

# update
def update(clsX,osD,lang):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █ █ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀   █▀█ █▀▀ █▀█ █▀█ █▀
    █▄█ █▀▀ █▄▀ █▀█  █  ██▄   █▀▄ ██▄ █▀▀ █▄█ ▄█
        """)
    print(" ")
    print(Fore.RED+f"{lang['update']}")
    print(" ")
    		# os.system("sudo apt update && clear")
    os.system(gencommand(osD,'update','none'))
    cls(clsX)

# upgrade
def upgrade(clsX,osD,lang):
    cls(clsX)
    print(" ")
    print(Fore.GREEN + """
    █ █ █▀█ █▀▀ █▀█ ▄▀█ █▀▄ █▀▀   ▄▀█ █   █     █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀ █▀
    █▄█ █▀▀ █▄█ █▀▄ █▀█ █▄▀ ██▄   █▀█ █▄▄ █▄▄   █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄ ▄█
        """)
    print(" ")
    print(Fore.RED+f"{lang['upgrade']}")
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
def chos(clsX,osD,spkg,userOS,commands,lang):
    cls(clsX)
    print(f"{userOS}: {osD} --> ?")
    print("")
    osss = osD
    print(f"{lang['spkg']}:")
    print("")
    welcomecomprint(spkg)
    print("")
    x = input(f"{lang['inputpkg']} :")
    osD = spkg[int(x)-1]
    print(f"{userOS}: {osss} --> {osD}")
    print(f"{lang['install']} :{commands['install'][osD]}")
    print(f"{lang['update']} :{commands['update'][osD]}")
    print(f"{lang['upgrade']} :{commands['upgrade'][osD]}")
    print(f"{lang['remove']} :{commands['remove'][osD]}")
    print("")
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
    print(f"cls(): {clssss} --> {clsX}")
    return clsX