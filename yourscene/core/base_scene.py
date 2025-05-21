from ursina import Entity, camera, destroy
from yourscene.ui.components.ui_title_bar import UITitleBar
from yourscene.ui.ui_manager import ui_manager

class BaseScene:
    def __init__(self, scene_manager=None):
        self.scene_manager = scene_manager
        self.ui_root = None
        self.title_bar = None
        self.window = None  # ⬅⬅⬅ to chroni przed błędem

    def input(self, key):
        """Opcjonalna metoda do nadpisania w klasach potomnych."""
        pass

    def bind_input(self):
        """Metoda pomocnicza — można nadpisać w scenie potomnej, żeby przypiąć skróty."""
        pass

    def on_enter(self):
        print("[BASE] BaseScene.on_enter() działa")
        self.ui_root = Entity(parent=camera.ui)
        show_menu = self.__class__.__name__ != 'MenuScene'
        self.title_bar = UITitleBar(scene_manager=self.scene_manager, parent=self.ui_root, show_menu_button=show_menu)

        print(f"[BASE] próbuję odpalić bind_input z: {self.__class__.__name__}")
        try:
            self.bind_input()
        except Exception as e:
            print(f"[ERROR] bind_input nie zadziałało: {e}")


    def on_exit(self):
        ui_manager.close_all()

        for child in list(camera.ui.children):
            destroy(child)

        if self.ui_root:
            destroy(self.ui_root)
            self.ui_root = None

        self.title_bar = None

        # Czyścimy bindy z InputManagera
        if self.scene_manager and hasattr(self.scene_manager, 'app'):
            self.scene_manager.app.input_manager.clear()


