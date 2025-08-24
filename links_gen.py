import random
import os.path

# Функция для генерации случайной ссылки
def generate_random_link(link_type: str, yt_type='Default') -> str:
    match link_type:
        case 'Telegram':
            link: str = f'https://t.me/+/{"".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_", k=16))}'
        case 'Discord':
            link: str = f'https://discord.gg/{"".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))}'
        case 'Youtube':
            match yt_type:
                case 'Default':
                    link: str = f'https://www.youtube.com/{"".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                                                                                    k=random.randint(11, 12)))}'
                case 'Shorts':
                    link: str = f'https://www.youtube.com/shorts/{''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                                                                                    k=11))}'
    return link

def generate_links(links_num: int, link_type: str, rewrite: bool, yt_type='Default') -> None:
    # если файла нет, создаем
    if os.path.exists('links.txt') == False:
        with open('links.txt', 'w+') as f:
            ...
    
    # запись ссылок в файл
    mode = 'w+' if rewrite == True else 'a+' # если чекбокс перезаписи активен, то w+
    with open('links.txt', mode) as f: # генерация ссылок
        for link in range(1, links_num + 1): # цикл генерации ссылок
            f.write(f'{generate_random_link(link_type, yt_type)}\n')


if __name__ == '__main__':
    ...
