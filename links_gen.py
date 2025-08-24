import random
import os.path


# стандартные символы
standart_symbs: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
standart_symbs_lower: str = 'abcdefghijklmnopqrstuvwxyz0123456789'

# функция для генерации случайной ссылки
def generate_random_link(link_type: str, yt_type='Default') -> str:
    match link_type:
        case 'Telegram':
            link: str = f'https://t.me/+{''.join(random.choices(standart_symbs + '_', k=16))}'
        case 'Discord':
            link: str = f'https://discord.gg/{''.join(random.choices(standart_symbs, k=8))}'
        case 'Youtube':
            match yt_type:
                case 'Default':
                    link: str = f'https://www.youtube.com/{''.join(random.choices(standart_symbs, k=random.randint(11, 12)))}'
                case 'Shorts':
                    link: str = f'https://www.youtube.com/shorts/{''.join(random.choices(standart_symbs, k=11))}'
        case 'TikTok':
            link: str = f'https://vm.tiktok.com/Z{''.join(random.choices(standart_symbs, k=8))}'
        case 'Rutube':
            link: str = f'https://rutube.ru/video/{''.join(random.choices(standart_symbs_lower, k=32))}'
        case 'Bitly':
            link: str = f'https://bit.ly/{''.join(random.choices(standart_symbs, k=7))}'
    return link

def generate_links(links_num: int, link_type: str, rewrite: bool, yt_type='Default') -> None:
    # если файла нет, создаем
    if not os.path.exists('links.txt'):
        with open('links.txt', 'w+') as f:
            ...

    # запись ссылок в файл
    mode = 'w+' if rewrite == True else 'a+' # если чекбокс перезаписи активен, то w+
    with open('links.txt', mode) as f: # генерация ссылок
        for _ in range(1, links_num + 1): # цикл генерации ссылок
            f.write(f'{generate_random_link(link_type, yt_type)}\n')

