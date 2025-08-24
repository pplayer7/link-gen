import random
import os.path
import datetime

# Функция для генерации случайной ссылки
def generate_random_link(link_type: str) -> str:
    match link_type:
        case 'Telegram':
            link: str = "https://t.me/+" + "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_", k=16))
        case 'Discord':
            link: str = "https://discord.gg/" + "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))
        case 'Youtube':
            link: str = "https://www.youtube.com/" + "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=random.randint(11, 12)))
    return link

gen_time: float = 0.0

def generate_links(links_num: int, link_type: str, rewrite: bool) -> float:
    global gen_time

    # начинаем таймер
    start = datetime.datetime.now()

    # если файла нет, создаем
    if os.path.exists('links.txt') == False:
        with open('links.txt', 'w+') as f:
            ...
    
    # запись ссылок в файл
    mode = 'w+' if rewrite == True else 'a+' # если чекбокс перезаписи активен, то w+
    with open('links.txt', mode) as f: # генерация ссылок
        for link in range(1, links_num + 1):
            link = generate_random_link(link_type)
            f.write(f'{link}\n')

    finish = datetime.datetime.now()

    gen_time = finish - start


if __name__ == '__main__' :
    ...
