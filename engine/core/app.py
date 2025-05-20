
from ursina import Ursina
from engine.core.scene_manager import SceneManager
from engine.plugins.loader import load_plugins
from game.scenes.menu_scene import MenuScene
from game.scenes.game_scene import GameScene

class GameApp:
    def __init__(self):
        print("[INIT] Tworzenie aplikacji gry")
        self.app = Ursina()

        self.scene_manager = SceneManager()
        self.scene_manager.add_scene("menu", MenuScene(self.scene_manager))
        self.scene_manager.add_scene("game", GameScene(self.scene_manager))

        self.plugins = load_plugins()
        for plugin in self.plugins:
            plugin.activate()

        self.app.update = self.update

    def run(self):
        print("[RUN] Uruchamianie aplikacji")
        self.scene_manager.set_scene("menu")
        self.app.run()

    def update(self):
        for plugin in self.plugins:
            if hasattr(plugin, "update"):
                plugin.update()
        self.scene_manager.update()