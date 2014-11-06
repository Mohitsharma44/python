from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation

Builder.load_string('''
<Simple>:
    the_label: _the_label
    RelativeLayout:
        Label:
            id: _the_label
            size_hint: 0.3, 0.1
            center_x: self.parent.width/2
            center_y: self.parent.height/2
            text: str( root.sometext )
    Button:
        text: '+++'
        on_release: root.animate()
''')


class Simple(BoxLayout):
    the_label = ObjectProperty(None)
    sometext = NumericProperty(5)

    def animate(self):
        left = Animation(x=0)
        left.bind(on_complete=self.inc)
        right = Animation(center_x=self.the_label.parent.width/2)
        anim = left + right
        anim.start(self.the_label)

    def inc(self, instance, value):
        self.sometext += 5 

class TApp(App):
    def build(self):
        return Simple()

TApp().run()
