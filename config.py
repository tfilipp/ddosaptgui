config = {
	'os': {
		'pacman': 'True',
        'pamac': 'False',
        'yay': 'False',
        'apt': 'False'
	},
	'clsX': True,
	'osAUTODETECT': True,
    # 'osAUTODETECT': False,
    'pkgautodetect': True,
    'lang': 'ru'
}
commands = {
    'install': {'pacman':'sudo pacman -S ','apt':'sudo apt install ','yay':'yay -S ','pamac':'sudo pamac install '},
    'update': {'pacman':'sudo pacman -Sy','apt':'sudo apt update','yay':'sudo yay -Sy','pamac':'sudo pamac update'},
    'upgrade': {'pacman':'sudo pacman -Syu','apt':'sudo apt upgrade','yay':'yay -Syu','pamac':'sudo pamac upgrade'},
    'remove': {'pacman':'sudo pacman -R ','apt':'sudo apt remove ','yay':'sudo yay -R ','pamac':'sudo pamac remove '}
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
        'pkgname': 'Package name',
        'spkg':'Supported package managers in system',
        'inputpkg':'Input a number of package manager',
        'changelang': 'Change language',
        'inputlang': 'Input lang (ru/en)'
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
        'pkgname': 'Имя пакета',
        'spkg':'Поддерживаемые пакетные менеджеры',
        'inputpkg':'Введите номер пакетного менеджера',
        'changelang':'Поменять язык',
        'inputlang': 'Введите язык (ru/en)'
    }
}