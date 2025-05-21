from ursina import *
from yourscene.core.base_scene import BaseScene
from yourscene.ui.components.button import UIButton

class GameScene(BaseScene):
    def __init__(self, manager):
        super().__init__(scene_manager=manager)
        self.manager = manager
        self.ui_root = None
        self.button = None

    def on_enter(self):
        print("[GAME] Start gry")
        super().on_enter() # górny pasek
 

    def on_exit(self):
        print("[MENU] Wychodzenie z menu (on_exit)")

        if self.window:
            destroy(self.window)
            print("[MENU] Zniszczono okno menu")
            self.window = None
            
            
    def bind_input(self):
        self.manager.app.input_manager.bind('escape', self.return_to_menu)


    def update(self):
        pass
