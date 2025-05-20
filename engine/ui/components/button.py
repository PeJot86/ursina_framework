from ursina import Entity, Text, camera, color, Func, destroy

class UIButton(Entity):
    def __init__(self, text='OK', parent=None, scale=(0.3, 0.1), position=(0, 0), on_click=None):
        super().__init__(
            parent=parent or camera.ui,
            model='quad',
            color=color.azure,
            scale=scale,
            position=position,
            collider='box',
            z=-0.9
        )

        self.label = Text(
            text=text,
            parent=camera.ui,
            origin=(0, 0),
            scale=1,
            z=-1.1,
            color=color.black
        )

        self.on_click = Func(on_click) if on_click else None

    def input(self, key):
        if self.hovered and key == 'left mouse up':
            if self.on_click:
                self.on_click()

    def update(self):
        self.color = color.lime if self.hovered else color.azure
        self.label.world_position = self.world_position  

    def on_destroy(self):
        destroy(self.label)
