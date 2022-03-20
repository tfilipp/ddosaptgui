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

		libs.welcomecomprint([
			lang['install'],
			lang['remove'],
			lang['update'],
			lang['upgrade'],
			lang['about'],
			lang['edit']['os'],
			lang['edit']['cls'],
			lang['exit']
		])
		print('')
		i=input(f"{lang['select']}>>>")
		if i == "1":
			libs.install(clsX,osD,lang)
		elif i == "2":
			libs.deletee(clsX,osD,lang)
		elif i == "3":
			libs.update(clsX,osD,lang)
		elif i == "4":
			libs.upgrade(clsX,osD,lang)
		elif i == "5":
			libs.about(clsX)
		elif i == "6":
			osD = libs.chos(clsX,osD)
		elif i == "7":
			clsX = libs.clsXc(clsX)
		elif i == "8":
			libs.ext(clsX)
		else:
			libs.cls(clsX)
			welcome(osD)
			print (" ")
			print (Fore.RED + f"{lang['input']}")
			print (" ")

if __name__ == '__main__':
	main()
