from ursina import Entity, camera, destroy
from engine.ui.components.ui_title_bar import UITitleBar

class BaseScene:
    def __init__(self):
        self.ui_root = None
        self.title_bar = None

    def on_enter(self):
        self.ui_root = Entity(parent=camera.ui)
        self.title_bar = UITitleBar(parent=self.ui_root)

    def on_exit(self):
        if self.ui_root:
            destroy(self.ui_root)
            self.ui_root = None
            self.title_bar = None

    def update(self):
        pass
