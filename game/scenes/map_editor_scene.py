from ursina import *
from game.scenes.base_scene import BaseScene

class MapEditorScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager
        self.tiles = []
        self.camera = None
        self.ui_root = None

    def on_enter(self):
        print("[EDITOR] Wchodzenie do edytora mapy")

        # Ustawienie kamery edytora
        self.camera = EditorCamera()
        self.camera.position = (0, 20, -20)
        self.camera.rotation_x = 45

        # Tworzenie siatki 10x10
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

        # UI: Przycisk powrotu
        self.ui_root = Entity(parent=camera.ui)
        self.back_button = Button(
            text="Wróć do menu",
            parent=self.ui_root,
            scale=(0.2, 0.08),
            position=(-0.7, 0.45),
            on_click=self.return_to_menu
        )

    def return_to_menu(self):
        self.manager.set_scene("menu")

    def update(self):
        if mouse.left:
            hit = mouse.hovered_entity
            if hit and hit in sum(self.tiles, []):
                hit.color = color.azure

    def on_exit(self):
        print("[EDITOR] Wychodzenie z edytora")
        for row in self.tiles:
            for tile in row:
                destroy(tile)
        self.tiles.clear()
        if self.camera:
            destroy(self.camera)
            self.camera = None
        if self.ui_root:
            destroy(self.ui_root)
            self.ui_root = None
