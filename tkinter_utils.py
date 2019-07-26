from tkinter import Menu, END
from tkinter.scrolledtext import ScrolledText
import logging
import time


def menu_builder(root, menu_blueprint, start=True, **kwargs):
    if start:
        menu_bar = root
    else:
        menu_bar = Menu(root, **kwargs)

    for sub in menu_blueprint:
        kw = sub.copy()
        del kw['name']
        if callable(sub.get('func')):
            del kw['func']
            logging.getLogger().info('kw: {}'.format(kw))
            menu_bar.add_command(label=sub['name'], command=sub['func'], **kw)
        else:
            del kw['sub']
            menu_bar.add_cascade(
                label=sub['name'], menu=menu_builder(menu_bar,
                                                     sub['sub'],
                                                     start=False, **kw))

    return menu_bar


class TextInputer:

    def __init__(self, root):
        self.enter_widget = ScrolledText(root, height=1)

    def pack(self, *args, **kwargs):
        self.enter_widget.pack(*args, **kwargs)

    @property
    def text(self):
        return self.enter_widget.get('1.0', END)[:-1]

    @text.setter
    def text(self, new_text):
        self.enter_widget.delete('1.0', END)
        self.enter_widget.insert('1.0', new_text)
