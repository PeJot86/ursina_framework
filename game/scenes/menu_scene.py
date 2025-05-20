from ursina import *
from game.scenes.base_scene import BaseScene
from engine.ui.components.panel import UIPanel
from engine.ui.components.button import UIButton


class MenuScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager
        self.ui_root = None
        self.button = None



    def on_enter(self):
        print("[MENU] Wchodzenie do sceny menu")
        self.ui_root = Entity(parent=camera.ui)

        self.button = UIButton(
            text="Start",
            parent=self.ui_root,            
            position=(0, 0),
            scale=(0.4, 0.15),
            on_click=self.start_game
        )
        

    def start_game(self):
        if self.manager:
            print("[MENU] Przełączam do sceny 'game'")
            self.manager.set_scene("game")

    def on_exit(self):
        print("[MENU] Wychodzenie z menu")
        destroy(self.ui_root)
        self.ui_root = None
        self.button = None

    def update(self):
        pass
