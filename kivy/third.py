from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

class SelectScreen(BoxLayout):
    background_color_normal = ListProperty([1,1,1,1])
    background_color_down = ListProperty([0,1,0,1])
    
    def screen1(self):
        self.ids.screen2.background_color =self.background_color_normal
        self.ids.screen2.text = self.ids.screen2.text[:8]
        self.ids.screen3.background_color =self.background_color_normal
        self.ids.screen3.text = self.ids.screen3.text[:8]
        self.ids.screen4.background_color =self.background_color_normal
        self.ids.screen4.text = self.ids.screen4.text[:8]
        if(self.ids.screen1.state == "normal"):
            self.ids.screen1.text = self.ids.screen1.text + '\nSelected'
            self.screen1_options()

        else:
            self.ids.screen1.text = self.ids.screen1.text[:8]
            self.ids.screen1.background_color = self.background_color_down


        
    def screen2(self):
        self.ids.screen1.background_color =self.background_color_normal
        self.ids.screen1.text = self.ids.screen1.text[:8]
        self.ids.screen3.background_color =self.background_color_normal
        self.ids.screen3.text = self.ids.screen3.text[:8]
        self.ids.screen4.background_color =self.background_color_normal
        self.ids.screen4.text = self.ids.screen4.text[:8]
        if(self.ids.screen2.state == "normal"):
            self.ids.screen2.text = self.ids.screen2.text + '\nSelected'
            self.screen2_options()
        else:
            self.ids.screen2.text = self.ids.screen2.text[:8]
            self.ids.screen2.background_color = self.background_color_down
        #print "Calling from Screen2"
        #self.screen2_options
        
    def screen3(self):
        self.ids.screen1.background_color =self.background_color_normal
        self.ids.screen1.text = self.ids.screen1.text[:8]
        self.ids.screen2.background_color =self.background_color_normal
        self.ids.screen2.text = self.ids.screen2.text[:8]
        self.ids.screen4.background_color =self.background_color_normal
        self.ids.screen4.text = self.ids.screen4.text[:8]
        if(self.ids.screen3.state == "normal"):
            self.ids.screen3.text = self.ids.screen3.text + '\nSelected'
        else:
            self.ids.screen3.text = self.ids.screen3.text[:8]
            self.ids.screen3.background_color = self.background_color_down

        
    def screen4(self):
        self.ids.screen1.background_color =self.background_color_normal
        self.ids.screen1.text = self.ids.screen1.text[:8]
        self.ids.screen2.background_color =self.background_color_normal
        self.ids.screen2.text = self.ids.screen2.text[:8]
        self.ids.screen3.background_color =self.background_color_normal
        self.ids.screen3.text = self.ids.screen3.text[:8]
        if(self.ids.screen4.state == "normal"):
            self.ids.screen4.text = self.ids.screen4.text + '\nSelected'
        else:
            self.ids.screen4.text = self.ids.screen4.text[:8]
            self.ids.screen4.background_color = self.background_color_down



    def screen1_options(self):
        print "Screen1 Suboptions"
        s1b1 = Button(size_hint_y=None,
                      height=40, text='SubOption1',
                      background_color = self.background_color_normal)
        f= BoxLayout()
        f.add_widget(s1b1)
        
        

    def screen2_options(self):
        print "Screen2 Suboptions"

class dashboard(App):
    #background_color_normal = ListProperty([1,1,1,0.5])
    #background_color_down = ListProperty([1,0,0,1])
    def build(self):
        return SelectScreen()

if __name__ == '__main__':
    dashboard().run()
