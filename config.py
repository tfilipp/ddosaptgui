config = {
	'os': {
		'arch': True,
		'debian': False
	},
	'clsX': True,
	'osAUTODETECT': True,
    'lang': 'ru'
}
commands = {
    'install': {'arch':'sudo pacman -S ','debian':'sudo apt install '},
    'update': {'arch':'sudo pacman -Sy','debian':'sudo apt update'},
    'upgrade': {'arch':'sudo pacman -Syu','debian':'sudo apt upgrade'},
    'remove': {'arch':'sudo pacman -R ','debian':'sudo apt remove'}
}
translate = {
    'en': {
        'detectedOS':['detected OS','OS (in config)'],
        'action':'Choose action',
        'install':'Install package',
        'update': 'Update repos',
        'upgrade': 'Upgrade all packages',
        'remove': 'Remove package',
        'about': 'About',
        'edit': {
            'os': 'Change os',
            'cls': 'enable/disable cls()'
        },
        'exit':'Exit',
        'select':'Selection',
        'input':'Please check that you typed a NUMBER from 1-7.',
        'passwarn': 'You might input your password if you have not already.',
        'nocom': 'No commands',
        'noos': 'No os. EDIT commands, changeos and detectos function',
        'pkgname': 'Package name'
    },
    'ru': {
        'detectedOS':['Обнаруженая система','СИСТЕМА (в конфиге)'],
        'action':'Выберите действие',
        'install':'Установить пакет',
        'update': 'Обновить репозитории',
        'upgrade': 'Обновить пакеты',
        'remove': 'Удалить пакет',
        'about': 'О нас',
        'edit': {
            'os': 'Изменить систему',
            'cls': 'Включить/Выключить cls()'
        },
        'exit':'Выйти',
        'select':'Выбор',
        'input':'Проверьте что вы ввели цифру от 1 до 7.',
        'passwarn': 'Вводите пароль.',
        'nocom': 'Нет комманд',
        'noos': 'Такой системы нет :(. Поменяйте команды (в config.py), detectos,changeos (в libs.py)',
        'pkgname': 'Имя пакета'
    }
}