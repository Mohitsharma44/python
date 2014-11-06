from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.clock import Clock

class SelectScreen(BoxLayout):
    background_color_normal = ListProperty([1,1,1,1])
    background_color_down = ListProperty([1,0,0,1])
    count = 0
    def on_press(self):
        self.count = self.count + 1
        self.ids.btn1.background_color =self.background_color_down
        if(self.count%2!=0):
            self.ids.btn1.text = self.ids.btn1.text + '\nSelected'
            self.ids.btn1.background_color = self.background_color_down
        else:            
            self.ids.btn1.text = self.ids.btn1.text[:8]
            self.ids.btn1.background_color =self.background_color_normal
class dashboard(App):
    #background_color_normal = ListProperty([1,1,1,0.5])
    #background_color_down = ListProperty([1,0,0,1])
    def build(self):
        return SelectScreen()

if __name__ == '__main__':
    dashboard().run()
