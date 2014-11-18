from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

class AccordionApp(App):
    def build(self):
        root = Accordion(orientation="vertical")
        for x in range(4):
            item = AccordionItem(title='Screen %d' % x)
            item.add_widget(Button(text='Vis TimeLapse\n', size_hint=(0.25,0.25), 
                                   pos=(100, 100)))
            item.add_widget(Button(text='IR TimeLapse\n', size_hint=(0.25,0.25),
                                   pos=(100, 100)))
            item.add_widget(Button(text='Vis Live\n', size_hint=(0.25,0.25),
                                   pos=(100, 100)))
            item.add_widget(Button(text='IR Live\n', size_hint=(0.25,0.25),
                                   pos=(100, 100)))



            root.add_widget(item)
        return root

if __name__ == '__main__':
    AccordionApp().run()
