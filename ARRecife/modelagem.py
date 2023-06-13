from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton, MDIconButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from PIL import Image as PilImage

import webbrowser
from kivy3 import Renderer, Scene
from kivy3 import PerspectiveCamera

from kivy3.extras.geometries import BoxGeometry
from kivy3 import Material, Mesh
from kivy.core.window import Window

from kivy.uix.image import Image

Window.size = [350,600]

class My3D(MDApp):
    dialog = None

    def _adjust_aspect(self, *args):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def capture_image(self, *args):
        image = self.renderer.export_as_image()

        image.save("cubo3d.png")

    def rotate_cube(self, *dt):
        self.cube.rotation.y += 1

    def build(self):
        self.theme_cls.theme_style = "Dark"
        layout = FloatLayout()

        self.renderer = Renderer()

        scene = Scene()

        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material()
        self.cube = Mesh(
            geometry=cube_geo,
            material=cube_mat
        )
        self.cube.pos.z = -5

        self.camera = PerspectiveCamera(
            fov=75,  
            aspect=0, 
            near=1,   
            far=10   
        )

        scene.add(self.cube)
        self.renderer.render(scene, self.camera)

        self.renderer.bind(size=self._adjust_aspect)

        layout.add_widget(self.renderer)

        button = MDIconButton(
                                icon = "information-outline",
                                icon_size = "50sp", 
                                pos_hint={"center_x": 0.80, "center_y": 0.07}, 
                                on_release=self.show_dialog
                              )
        layout.add_widget(button)
        button1 = MDIconButton(
                                icon = "camera-outline",
                                icon_size = "64sp", 
                                pos_hint={"center_x": 0.50, "center_y": 0.07}, 
                                on_release=self.capture_image
                               )
        layout.add_widget(button1)
        button2 = MDIconButton(
                                icon = "keyboard-return",
                                icon_size = "50sp",
                                pos_hint={"center_x": 0.20, "center_y": 0.06}
                                )
        layout.add_widget(button2)

        retangulo = MDFloatLayout(
                                md_bg_color =(0,0,0,1), 
                                size_hint= (1, 0.15), 
                                opacity= 0.25
                                )
        layout.add_widget(retangulo)

        wimage = Image(
                    source="Image\detro.jpg", 
                    opacity =0.2
                       )
        layout.add_widget(wimage)

        Clock.schedule_interval(self.rotate_cube, .01)
        return layout
    
    def site(self, *args):
        try:
            webbrowser.open("https://visit.recife.br/o-que-fazer/atracoes/teatros/teatro-apolo")
        except:
            print("Site não encontrado")
    def show_dialog(self, *args):
        try:
            with open("teatro.txt", 'r', encoding='utf-8') as arquivo:
                a = arquivo.read() 
        except FileNotFoundError:
            print("Arquivo não encontrado!")
        if not self.dialog:
            button_ok = MDFlatButton(text="OK", 
                                     on_release=self.close_dialog
                                     )
            
            saiba = MDFlatButton(text='Saiba Mais', 
                                 on_release=self.site
                                 )

            self.dialog = MDDialog(title="Teatro Apolo", 
                                   text=a, 
                                   buttons=[button_ok, saiba]
                                   )
        self.dialog.open()

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
        
My3D().run()
