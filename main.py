import time
import os
import t2s

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class T2SFileExplorer(Screen):
    def load(self, path, filename):
        t2s.convertAudio(os.path.join(path, filename[0]))

class CameraClickForT2S(BoxLayout, Screen):
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

class YoloWindowCamera(BoxLayout, Screen):
    pass

class YoloWindowFileExplorer(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

MyMainApp().run()