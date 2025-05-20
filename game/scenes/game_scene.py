from ursina import *
from game.scenes.base_scene import BaseScene

class GameScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager
        self.ui_root = None
        self.button = None

    def on_enter(self):
        print("[GAME] Start gry")
        self.ui_root = Entity()
        self.button = Button(
            text="Menu",
            parent=self.ui_root,
            scale=(0.2, 0.1),
            y=-0.4,
            on_click=Func(self.return_to_menu)  # ✅ tu też używamy Func()
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
