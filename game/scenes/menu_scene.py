from ursina import *
from game.scenes.base_scene import BaseScene
from engine.ui.components.panel import UIPanel
from engine.ui.components.button import UIButton
from engine.ui.components.layout import UIColumn
from engine.ui.components.text_input import UITextInput
from engine.ui.components.window import UIWindow
from engine.ui.ui_manager import ui_manager
import time


class MenuScene(BaseScene):
    def __init__(self, manager):
        super().on_enter()
        self.manager = manager
        self.window = None
        self.last_esc_time = 0

    def on_enter(self):
        print("[MENU] Wchodzenie do sceny menu")

        self.window = UIWindow(title='Menu', size=(0.5, 0.4), position=(0, 0))
        ui_manager.open_window(self.window)

        self.column = UIColumn(parent=self.window, padding=0.05)
        self.column.y = 0.1

        self.name_input = UITextInput(placeholder='Imię', parent=self.window)
        self.start_button = UIButton(text='Nowa gra', scale=(0.3, 0.1), on_click=self.start_game, parent=self.window)
        self.editor_button = UIButton(
        text='Edytor',
        scale=(0.3, 0.1),
        on_click=self.start_editor,
        parent=self.window
        )
        self.button_exit = UIButton(text='Wyjdź', scale=(0.3, 0.1), on_click=application.quit, parent=self.window)

        self.column.add(self.name_input)
        self.column.add(self.start_button)
        self.column.add(self.editor_button)
        self.column.add(self.button_exit)

    def start_editor(self):
        self.manager.set_scene("editor")


    def update(self):
        if held_keys['escape'] and time.time() - self.last_esc_time > 0.3:
            self.last_esc_time = time.time()
            if self.window:
                ui_manager.toggle_window(self.window)

    def start_game(self):
        self.name = self.name_input.value
        print(f"Imię gracza: {self.name}")
        
        if self.window:
            ui_manager.close_window(self.window)  # ← czyści UI z ekranu
            self.window = None
        self.manager.set_scene("game")

    def on_exit(self):
        print("[MENU] Wychodzenie z menu")
        if self.window:
            destroy(self.window)
            self.window = None
