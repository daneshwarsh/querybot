# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
# Press the green button in the gutter to run the script.


from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import dp
from kivymd.app import MDApp
from chat2 import answering


Window.size = (350, 550)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class ChatBot(MDApp):
    def change_Screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"

    def response(self, *args):
        response = ""
        global screen_manager  # Declare screen_manager as a global variable

        # main.py
        i = NumericProperty(0)
        response = answering(value)
        self.i = response.count('\n') + 1   # Add this line




        chats_screen = screen_manager.get_screen('chats')
        text_input = chats_screen.ids.text_input
        command = Response(text=response, size_hint_x=.75 )
        chats_screen.chat_list.add_widget(command)

    def send(self):
        global size, halign, value
        screen_manager = self.root

        chats_screen = screen_manager.get_screen('chats')
        text_input = chats_screen.ids.text_input

        if text_input.text:
            value = text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            command = Command(text=value, size_hint_x=size, halign=halign)
            chats_screen.chat_list.add_widget(command)
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""


if __name__ == '__main__':
    # ChatBot.run()
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    chatbot_instance = ChatBot()
    chatbot_instance.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


