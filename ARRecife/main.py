from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import  Builder
from kivy.core.text import LabelBase
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDTextButton
Window.size = [350, 600]

class Gerenciar(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class Janela1(Screen):
    pass        

class Janela2(Screen):
    pass

class Janela3(Screen):
    pass

class MainApp(MDApp):
    def on_start(self):
        self.start()
        self.buttonstart()

    def modelagem(self, *args):
        pass

    def start(self, *args):
        anim = Animation(opacity = 0.7, duration = 1)
        anim += Animation(opacity = 0.7, duration = 3)
        anim += Animation(opacity = 0, duration = 1)
        anim.bind(on_complete=self.start)
        anim.start(self.root.get_screen('main').ids.text1)
        
    def buttonstart(self, *args):
        anim = Animation(opacity = 0, duration = 0)
        anim += Animation(opacity = 1, duration = 1)
        anim.start(self.root.get_screen('main').ids.button1)
        anim.start(self.root.get_screen('main').ids.button2)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('screen.kv')

try:
    MainApp().run()
except:
    print('Erro no processamento do arquivo')