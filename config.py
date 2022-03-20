config = {
	'os': {
		'arch': True,
		'debian': False
	},
	'clsX': True,
	'osAUTODETECT': True
}
commands = {
    'install': {'arch':'sudo pacman -S ','debian':'sudo apt install '},
    'update': {'arch':'sudo pacman -Sy','debian':'sudo apt update'},
    'upgrade': {'arch':'sudo pacman -Syu','debian':'sudo apt upgrade'},
    'remove': {'arch':'sudo pacman -R ','debian':'sudo apt remove'}
}