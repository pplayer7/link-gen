from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo, askyesno
from links_gen import *
from time import time

# root
root: Tk = Tk()
root.geometry('400x300')
root.title('Генератор ссылок')

# выбор типа ссылки
link_list: tuple = ('Telegram', 'Discord', 'Youtube') # варианты ссылок
# TODO: other social media
# TODO: README.md
standart_link: StringVar = StringVar() # стандартное значение для списка
standart_link.set(link_list[0])

link_combobox: ttk.Combobox = ttk.Combobox(values=link_list, state='readonly', textvariable=standart_link, width=15, height=3)
link_combobox.place(anchor=NW, relx=0.0, rely=0.0)

youtube_list: tuple = ('Default', 'Shorts') # список для ютуба

standart_youtube: StringVar = StringVar() # стандартное значение списка ютуба
standart_youtube.set(youtube_list[0])

youtube_combobox: ttk.Combobox = ttk.Combobox(values=youtube_list, state='readonly', textvariable=standart_youtube, width=15, height=3)

def yt_def_shorts(event) -> None:
    link_type = link_combobox.get()

    if link_type == 'Youtube':
        youtube_combobox.place(anchor=NE, relx=1.0, rely=0.0)
    else:
        youtube_combobox.destroy()

link_combobox.bind('<<ComboboxSelected>>', yt_def_shorts)

# кол-во ссылок
links_num: ttk.Entry = ttk.Entry(validate='key',
                                validatecommand=(root.register(lambda num: num.isdigit() or not num), '%P', ),
                                width=33) # лол, простой вериф
links_num.insert(0, 1)
links_num.place(anchor=CENTER, relx=1.0, rely=0.5)

# кнопка перезаписи
rewrite_state: BooleanVar = BooleanVar()
rewrite_button: ttk.Checkbutton = ttk.Checkbutton(text='Перезаписать?', variable=rewrite_state)
rewrite_button.place(anchor=SW, relx=0.0, rely=1.0)

# кнопка генерации
def gen_links_gui() -> None:
    if int(links_num.get()) >= 5_000_000: # если слишком ного ссылок (мб это просто для моего пк много)
        yes_no = askyesno(title='Внимание!', message='Создатель не ручается за генерацию такого большого количества ссылок! Продолжить?')
    elif int(links_num.get()) == 0: # если пользователь поставил ноль
        showwarning(title='Внимание!', message='Введите корректное значение!')
    else: # остальные случаи (отрицательных нет, потому что не могут ввести, лмао)
        yes_no = True

    if yes_no: # начало цикла

        start_time = time() # начало таймера

        generate_links(int(links_num.get()), link_combobox.get(), rewrite_state.get(), youtube_combobox.get()) # генерация ссылок в файл

        gen_time = round(time() - start_time, 6) # время генерации

        showinfo(title='Успех!', message=f'Ссылки успешно сгенерированы!\nВремя генерации: {gen_time}')

    else:
        ...


generate_button: ttk.Button = ttk.Button(text='Сгенерировать!', command=gen_links_gui, width=15)
generate_button.place(anchor=SE, relx=1.0, rely=1.0)


info_label: ttk.Label = ttk.Label(text='Количество ссылок')
info_label.place(anchor=E, relx=1.0, rely=0.4)

def main() -> None:
    root.mainloop()

if __name__ == '__main__':
    main()