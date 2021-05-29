import os

from files.wrn.warn import i_e_colo

try:
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo()

def credits():
    print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
    f'\t\t\thttps://vk.com/2pac_jdm\n'
    f'\t\t\thttps://vk.com/paket\n'
    f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
    print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
    print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
    f'\t\t\thttps://github.com/Ki11sesh\n'
    f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)

def test_credits():
    print()
    os.system("clear")
