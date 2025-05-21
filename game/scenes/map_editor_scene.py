from ursina import *
from yourscene.core.base_scene import BaseScene

class MapEditorScene(BaseScene):
    def __init__(self, manager):
        super().__init__(scene_manager=manager)
        self.manager = manager
        self.tiles = []
        self.camera = None

    def bind_input(self):
        print("[SCENE] bind_input() uruchomione!")  # ← powinno się pojawić!
        im = self.manager.app.input_manager
        im.bind('escape', self.return_to_menu)
        im.bind('ctrl+z', self.undo)
        im.bind('ctrl+s', self.quick_save)
        im.bind('ctrl+shift+s', self.save_as)

    def on_enter(self):
        print("[EDITOR] Wchodzenie do edytora mapy")
        print(f"[CHECK] Typ self: {type(self)}")
        print(f"[CHECK] bind_input pochodzi z: {self.bind_input.__func__.__qualname__}")
        print(f"[CHECK] BaseScene z którego dziedziczymy: {BaseScene}")

        super().on_enter()

        self.camera = EditorCamera()
        self.camera.position = (0, 20, -20)
        self.camera.rotation_x = 45

        for x in range(10):
            row = []
            for z in range(10):
                tile = Entity(
                    model='quad',
                    color=color.white33,
                    scale=(1, 1),
                    position=(x, 0, z),
                    rotation_x=90,
                    collider='box'
                )
                row.append(tile)
            self.tiles.append(row)

    def on_exit(self):
        print("[EDITOR] Wychodzenie z edytora")
        for row in self.tiles:
            for tile in row:
                destroy(tile)
        self.tiles.clear()
        if self.camera:
            destroy(self.camera)
            self.camera = None

    def update(self):
        if mouse.left:
            hit = mouse.hovered_entity
            if hit and hit in sum(self.tiles, []):
                hit.color = color.azure


    def return_to_menu(self):
        print("[SCENE] Powrót do menu")
        self.manager.set_scene("menu")

    def undo(self):
        print("[SCENE] Cofnięcie akcji")

    def quick_save(self):
        print("[SCENE] Szybki zapis")

    def save_as(self):
        print("[SCENE] Zapisz jako...")
