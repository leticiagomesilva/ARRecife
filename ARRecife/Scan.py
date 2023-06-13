from kivymd.app import MDApp
from kivy.lang import Builder
from pyzbar.pyzbar import ZBarSymbol
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
Window.size = [350, 600]

KV = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
MDBoxLayout:
    ZBarCam:
        id:zbarcam
        code_types:ZBarSymbol.QRCODE.value,ZBarSymbol.EAN13.value
        on_symbols:app.on_symbols(*args)

"""


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.root = Builder.load_string(KV)
        

    def on_symbols(self,instance,symbols):
        if not symbols == "":
            for symbol in symbols:
                code = (symbol.data.decode())
                if code == 'Modelagem':
                    print("")
                Snackbar(
                text="{}".format(symbol.data.decode()),
                font_size=25
                ).open()

if __name__ == "__main__":
    MyApp().run()