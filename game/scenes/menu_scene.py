from ursina import *
from game.scenes.base_scene import BaseScene
from engine.ui.components.panel import UIPanel
from engine.ui.components.button import UIButton
from engine.ui.components.layout import UIColumn
from engine.ui.components.text_input import UITextInput
from engine.ui.components.window import UIWindow


class MenuScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager
        self.ui_root = None
        self.button = None


    def on_enter(self):
        print("[MENU] Wchodzenie do sceny menu")

        self.window = UIWindow(title='Nowa Gra', size=(0.5, 0.4), position=(0, 0))
        self.ui_root = self.window  # ← jeśli potrzebujesz kompatybilności z resztą kodu
        

        self.column = UIColumn(parent=self.window, padding=0.05)
        self.column.y = 0.1

        self.name_input = UITextInput(placeholder='Imię', parent=self.window)
        self.start_button = UIButton(text='Start', scale=(0.3, 0.1), on_click=self.start_game, parent=self.window)
        self.button_exit = UIButton(text='Wyjdź', scale=(0.3, 0.1), on_click=application.quit, parent=self.window)


        self.column.add(self.name_input)
        self.column.add(self.start_button)
        self.column.add(self.button_exit)



    def start_game(self):
        self.name = self.name_input.value
        print(f"Imię gracza: {self.name}")
        self.manager.set_scene("game")
        
    def input(self, key):
        if key == 'escape':
            print("[DEBUG] ESC wciśnięty — próbuję zamknąć okno")
            if hasattr(self, 'window') and self.window:
                self.window.close()
                self.window = None



    def on_exit(self):
        print("[MENU] Wychodzenie z menu")
        destroy(self.ui_root)
        self.ui_root = None
        self.button = None

    def update(self):
        pass
