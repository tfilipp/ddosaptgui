from colorama import Fore,init
import libs,config


init(autoreset=True)


def main():
	if config.config['osAUTODETECT']:
		osD = libs.detectOS()
	else:
		fq =  config.config['os']
		if fq['arch']:
			osD = 'arch'
		elif fq['debian']:
			osD = 'debian'
	if config.config['clsX']:
		clsX = True
	else:
		clsX = False
	libs.cls(clsX)
	welcome(osD)
	select(osD,clsX)

def welcome(osD):
	if osD == 'debian':
		print (Fore.GREEN + """

		█▀▄ █▀▄ █▀█ █▀   ▄▀█ █▀█ ▀█▀  █▀▀ █ █ █
		█▄▀ █▄▀ █▄█ ▄█   █▀█ █▀▀  █   █▄█ █▄█ █
		""")
		print(Fore.BLUE + "               ==========================================")
	else:
		print (Fore.GREEN + """

		█▀▄ █▀▄ █▀█ █▀  █▀█ █▄▀ █▀▀  █▀▀ █ █ █
		█▄▀ █▄▀ █▄█ ▄█  █▀▀ █ █ █▄█  █▄█ █▄█ █
		""")

		print(Fore.BLUE + "               ========================================")
	if config.config['osAUTODETECT']:
		print(f"                detected OS: {osD} ")	
	else:
		print(f"                OS (in config): {osD} ")	
	print(" ")

def select(osD,clsX):
	while (True):
		print("Choose action:")
		print (" ")
		print("""
			1. Install package
			2. Update repos
			3. Upgrade all packages
			4. About
			5. Change os
			6. enable/disable cls()
			7. Exit




			""")
		i=input("Selection>>>")
		if i == "1":
			libs.install(clsX,osD)
		elif i == "2":
			libs.update(clsX,osD)
		elif i == "3":
			libs.upgrade(clsX,osD)
		elif i == "4":
			libs.about(clsX)
		elif i == "5":
			osD = libs.chos(clsX,osD)
		elif i == "6":
			clsX = libs.clsXc(clsX)
		elif i == "7":
			libs.ext(clsX)
		else:
			libs.cls(clsX)
			welcome(osD)
			print (" ")
			print (Fore.RED + "Please check that you typed a NUMBER from 1-7.")
			print (" ")

if __name__ == '__main__':
	main()
