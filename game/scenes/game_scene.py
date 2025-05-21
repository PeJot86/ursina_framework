from ursina import *
from game.scenes.base_scene import BaseScene
from engine.ui.components.button import UIButton

class GameScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager
        self.ui_root = None
        self.button = None

    def on_enter(self):
        print("[GAME] Start gry")
        self.ui_root = Entity(parent=camera.ui)

        self.back_button = Button(
            text="Wróć do menu",
            parent=self.ui_root,
            scale=(0.2, 0.08),
            position=(-0.7, 0.45),
            on_click=self.return_to_menu
        )

    def return_to_menu(self):
        print("[GAME] Powrót do menu")
        self.manager.set_scene("menu")

    def on_exit(self):
        print("[GAME] Koniec gry")
        destroy(self.ui_root)
        self.ui_root = None
        self.button = None

    def update(self):
        pass
