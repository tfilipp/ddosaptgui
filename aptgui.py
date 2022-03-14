import os
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style 
print (Fore.GREEN + """

	█▀▄ █▀▄ █▀█ █▀   ▄▀█ █▀█ ▀█▀   █▀▀ █ █ █
	█▄▀ █▄▀ █▄█ ▄█   █▀█ █▀▀  █    █▄█ █▄█ █
""")
print(Fore.BLUE + "       ==========================================")
print(" ")
while (True):
	print("Choose action:")
	print (" ")
	print("""
		1. Install package
		2. Update repos
		3. Upgrade all packages
		4. About
		5. Exit




		""")
	i=input("Selection>>>")

	if (i=="1"):
		os.system("clear")
		print(" ")
		print(Fore.GREEN + """
		█ █▄ █ █▀ ▀█▀ ▄▀█ █   █     █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀
		█ █ ▀█ ▄█  █  █▀█ █▄▄ █▄▄   █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄
		""")
		print(" ")
		print(Fore.RED+"You might input your password if you have not already.")
		print(" ")
		ip=input("Package name>>>")
		os.system("sudo apt install " + ip)

	elif (i=="2"):
		os.system("clear")
		print(" ")
		print(Fore.GREEN + """
		█ █ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀   █▀█ █▀▀ █▀█ █▀█ █▀
		█▄█ █▀▀ █▄▀ █▀█  █  ██▄   █▀▄ ██▄ █▀▀ █▄█ ▄█
			""")
		print(" ")
		print(Fore.RED+"You might input your password if you have not already.")
		print(" ")
		os.system("sudo apt update && clear")

	elif (i=="3"):
		os.system("clear")
		print(" ")
		print(Fore.GREEN + """
		█ █ █▀█ █▀▀ █▀█ ▄▀█ █▀▄ █▀▀   ▄▀█ █   █     █▀█ ▄▀█ █▀▀ █▄▀ ▄▀█ █▀▀ █▀▀ █▀
		█▄█ █▀▀ █▄█ █▀▄ █▀█ █▄▀ ██▄   █▀█ █▄▄ █▄▄   █▀▀ █▀█ █▄▄ █ █ █▀█ █▄█ ██▄ ▄█
			""")
		print(" ")
		print(Fore.RED+"You might input your password if you have not already.")
		print(" ")
		os.system("sudo apt upgrade && clear")
	elif (i=="4"):
		print(" ")
		print(Fore.GREEN + """
		
		▄▀█ █▄▄ █▀█ █ █ ▀█▀
		█▀█ █▄█ █▄█ █▄█  █ 
		""")
		print(" ")
		print("""
			ddOS apt GUI v 0.0.1
			Created by coolamoeba
			""")
	elif (i=="5"):
		os.system("clear")
		exit()
	else:
		print (" ")
		print (Fore.RED + "Please check that you typed a NUMBER from 1-5.")
		print (" ")