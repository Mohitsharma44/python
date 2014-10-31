from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.image import Image

Builder.load_string(''' 

<CustomLayout>
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            texture: self.background_image.texture
            pos: self.pos
            size: self.size

<RootWidget>
    CustomLayout:
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
        Label:
            text: "This is Text1"
            text_size: self.width-20, self.height-20
            valign: 'top'

        Label:                                                                                     
            text: "This is Text1"                                                                  
            text_size: self.width-20, self.height-20                                                
            valign: 'middle'
            halign: 'center'

        Label:
            text: "This is Text1"                                                                  
            text_size: self.width-20, self.height-20                                               
            valign: 'bottom'
            halign: 'justify'

    Scatter:
        Button:
            on_press: root.btn1pressed()
            id: btn1
            bg_color: root.btn_color
            text: "Click Me"
            text_color:root.text_color
            size_hint: .1,.1
''')


class CustomLayout(GridLayout):
    background_image = ObjectProperty(
        Image(
            source = '/usr/share/kivi-examples/widgets/sequenced_images/data/images/button_white.png'))

class RootWidget(FloatLayout):
    text_color = ListProperty([1,1,1,1])
    btn_color = ListProperty([0.5,0.5,0.5,1])
    def btn1pressed(self):
        #print "Button CLicked"
        self.ids.btn1.text = "You Clicked Me!"
        #self.ids.btn1.color


class btn1(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    btn1().run()
