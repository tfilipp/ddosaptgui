from colorama import Fore,init
import libs,config


init(autoreset=True)


def main():
	lang = config.config['lang']
	langpkg = config.translate[lang]
	if config.config['osAUTODETECT']:
		osD,userOS = libs.detectOS()
		if osD == 'noos':
			print(langpkg['noos'])
			exit()
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
	welcome(osD,langpkg,userOS)
	select(osD,clsX,langpkg)

def welcome(osD,lang,userOS):
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
		print(f"                {lang['detectedOS'][0]}: {userOS} ")	
	else:
		print(f"                {lang['detectedOS'][1]}: {osD}/*-based ")	
	print(" ")

def select(osD,clsX,lang):
	while (True):
		print(f"{lang['action']}:")
		print (" ")
		print(f"1. {lang['install']}\n2. {lang['update']}\n3. {lang['upgrade']}\n4. {lang['about']}\n5. {lang['edit']['os']}\n6. {lang['edit']['cls']}\n7. {lang['exit']}")
		print("""




			""")
		i=input(f"{lang['select']}>>>")
		if i == "1":
			libs.install(clsX,osD,lang)
		elif i == "2":
			libs.update(clsX,osD,lang)
		elif i == "3":
			libs.upgrade(clsX,osD,lang)
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
			print (Fore.RED + f"{lang['input']}")
			print (" ")

if __name__ == '__main__':
	main()
