import kivy
from kivy.app import App
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from app import LoadScreen


# class CoverImage(CoverBehavior, Image):
#     """Image using cover behavior.
#     """

#     def __init__(self, **kwargs):
#         super(CoverImage, self).__init__(**kwargs)
#         texture = self._coreimage.texture
#         self.reference_size = texture.size
#         self.texture = texture

class PbApp(App):

    def build(self):
        return LoadScreen()


PbApp().run()
