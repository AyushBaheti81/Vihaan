import time

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import t2s


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CameraClick(BoxLayout, Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        clickedPhoto = "IMG_{}.jpg".format(timestr)
        camera.export_to_png(clickedPhoto)
        t2s.convertAudio(clickedPhoto)
        print("Captured")

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

MyMainApp().run()
