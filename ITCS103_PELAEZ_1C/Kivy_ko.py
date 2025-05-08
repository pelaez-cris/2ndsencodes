import kivy
from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):

    def build(self):

        return Label(text="Kivyng Basa")
HelloKivy = HelloKivy()
HelloKivy.run()
                                      