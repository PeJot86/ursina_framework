from ursina import *
from yurscene.core.base_scene import BaseScene

class MapEditorScene(BaseScene):
    def __init__(self, manager):
        super().__init__(scene_manager=manager)
        self.manager = manager
        self.tiles = []
        self.middle_drag = False
        self.right_drag = False

    def bind_input(self):
        print("[SCENE] bind_input() uruchomione!")
        im = self.manager.app.input_manager
        im.bind('escape', self.return_to_menu)
        im.bind('ctrl+z', self.undo)
        im.bind('ctrl+s', self.quick_save)
        im.bind('ctrl+shift+s', self.save_as)

    def on_enter(self):
        print("[EDITOR] Wchodzenie do edytora mapy")
        super().on_enter()

        camera.position = (0, 20, -20)
        camera.rotation = (45, 0, 0)
        camera.orthographic = False
        camera.fov = 60

        # Tworzenie siatki 10x10 kafli
        for x in range(10):
            for z in range(10):
                tile = Entity(
                    model='quad',
                    color=color.white33,
                    scale=(1, 1),
                    position=(x, 0, z),
                    rotation_x=90,
                    collider='box'
                )
                self.tiles.append(tile)

    def on_exit(self):
        print("[EDITOR] Wychodzenie z edytora")
        for tile in self.tiles:
            destroy(tile)
        self.tiles.clear()

    def update(self):
        if self.middle_drag:
            camera.x -= mouse.velocity[0] * 50
            camera.z += mouse.velocity[1] * 50

        if self.right_drag:
            camera.rotation_y += mouse.velocity[0] * 100
            camera.rotation_x -= mouse.velocity[1] * 100
        if self.middle_drag:
            print("[DEBUG] przesuwanie kamery aktywne")

    def input(self, key):
        if key == 'middle mouse down':
            self.middle_drag = True
            print('🎯 Środkowy wciśnięty')
        elif key == 'middle mouse up':
            self.middle_drag = False
            print('✅ Środkowy puszczony')

        if key == 'right mouse down':
            self.right_drag = True
            print('🎯 Prawy wciśnięty')
        elif key == 'right mouse up':
            self.right_drag = False
            print('✅ Prawy puszczony')

        if key == 'scroll up':
            camera.position += camera.forward * 2
        elif key == 'scroll down':
            camera.position -= camera.forward * 2

        elif key == 'left mouse down':
            hit = mouse.hovered_entity
            if hit and hit in self.tiles:
                print(f"[EDITOR] Kliknięto kafel: {hit.position}")
                hit.color = color.green

    def return_to_menu(self):
        print("[SCENE] Powrót do menu")
        self.manager.set_scene("menu")

    def undo(self):
        print("[SCENE] Cofnięcie akcji")

    def quick_save(self):
        print("[SCENE] Szybki zapis")

    def save_as(self):
        print("[SCENE] Zapisz jako...")
