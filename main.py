from tkinter import *
from tkinter import ttk
from links_gen import *

# root
root: Tk = Tk()
root.geometry('400x300+495+270')
root.title('Генератор ссылок')

# сообщение об успехе
success: Tk = Tk()
success.geometry('200x150+297+135')
success.title('Успех!')

# выбор типа ссылки
link_list: list = ['Telegram', 'Discord', 'Youtube']

standart_link: StringVar = StringVar() # стандартное значение
standart_link.set(link_list[0])

link_combobox: ttk.Combobox = ttk.Combobox(values=link_list, state='readonly', textvariable=standart_link)
link_combobox.pack(root, anchor=NW, padx=6, pady=6)

# кол-во ссылок
links_num: ttk.Entry = ttk.Entry(validate='key', validatecommand=(root.register(lambda num: num.isdigit() or not num), '%P')) # лол, простой вериф
links_num.insert(0, 1)
links_num.pack(root, anchor=SE, expand=True)

# кнопка перезаписи
rewrite_state: BooleanVar = BooleanVar()
rewrite_button: ttk.Checkbutton = ttk.Checkbutton(text='Перезаписать?', variable=rewrite_state)
rewrite_button.pack(root, anchor=SW, padx=2, pady=2)

# кнопка генерации
def gen_links_gui():
    generate_links(int(links_num.get()), link_combobox.get(), rewrite_state.get()) # генерация ссылок в файл
    success_label: ttk.Label = ttk.Label(text='Ссылки успешно сгенерированы!')
    time_of_generation: ttk.Label = ttk.Label(text=f'Время генерации: {gen_time}')
    success_label.pack(success, anchor=CENTER)
    time_of_generation.pack(success, anchor=CENTER)
    success.mainloop()


generate_button: ttk.Button = ttk.Button(text='Сгенерировать!',
                                        command=gen_links_gui)
generate_button.pack(root, anchor=SE, expand=True)



def main() -> None:
    root.mainloop()

if __name__ == '__main__':
    main()