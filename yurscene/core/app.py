from ursina import Ursina, color, window, Entity, mouse
from yurscene.core.scene_manager import SceneManager
from yurscene.core.input_manager import InputManager
from yurscene.plugins.loader import load_plugins
from game.scenes.menu_scene import MenuScene
from game.scenes.game_scene import GameScene
from yurscene.editor.map_editor_scene import MapEditorScene

class GameApp:
    def __init__(self):
        print("[INIT] Tworzenie aplikacji gry")
        self.app = Ursina()
        
        window.size = (1280, 720)
        window.position = (100, 100)
        window.fullscreen = False
        window.borderless = False
        window.color = color.black

        self.input_manager = InputManager()
        
        self.scene_manager = SceneManager(app=self)
        self.scene_manager.add_scene("menu", MenuScene(self.scene_manager))
        self.scene_manager.add_scene("game", GameScene(self.scene_manager))
        self.scene_manager.add_scene("editor", MapEditorScene(self.scene_manager))

        self.plugins = load_plugins()
        for plugin in self.plugins:
            plugin.activate()

        # Globalne bindy
        self.input_manager.bind('f12', lambda: print("[DEBUG] Zrzut debugowy (F12)"))

        self.app.update = self.update

    def run(self):
        print("[RUN] Uruchamianie aplikacji")
        self.scene_manager.set_scene("menu")
        self.app.run()

    def update(self):
        mouse.update()  # ← To naprawia mouse.velocity i hovered_entity
        for plugin in self.plugins:
            if hasattr(plugin, "update"):
                plugin.update()
        self.scene_manager.update()

    def input(self, key):
        print(f"[DEBUG] input: {key}")

        if ' up' in key:
            self.input_manager.release(key.replace(' up', ''))
        else:
            self.input_manager.handle(key)

        if self.scene_manager.current_scene and hasattr(self.scene_manager.current_scene, 'input'):
            self.scene_manager.current_scene.input(key)



