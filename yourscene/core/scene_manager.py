
class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        if self.current_scene:
            print(f"[MENU] Wychodzenie z {self.current_scene}")
            self.current_scene.on_exit()
        self.current_scene = self.scenes.get(name)
        if self.current_scene:
            print(f"[MENU] Przełączam do sceny '{name}'")
            self.current_scene.on_enter()

    def update(self):
        if self.current_scene:
            self.current_scene.update()
