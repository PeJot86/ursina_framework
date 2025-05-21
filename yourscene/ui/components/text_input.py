from ursina import Entity, Text, color, Func, time, mouse, camera, destroy

class UITextInput(Entity):
    def __init__(self, default_text='', placeholder='Wpisz...', scale=(0.3, 0.1), on_submit=None, parent=None, **kwargs):
        super().__init__(
            parent=parent or camera.ui,
            model='quad',
            color=color.white33,
            scale=scale,
            collider='box',
            z=-0.9,
            **kwargs
        )

        self.text_entity = Text(
            text=default_text or placeholder,
            parent=camera.ui,
            origin=(0, 0),
            z=-1.0,
            color=color.black
        )
        
        self.value = default_text
        self.placeholder = placeholder
        self.active = False
        self.on_submit = Func(on_submit) if on_submit else None
        self.cursor_blink = 0

    def input(self, key):
        if not self.active:
            return

        if key == 'enter':
            if self.on_submit:
                self.on_submit(self.value)
            self.active = False
            return

        if key == 'backspace':
            self.value = self.value[:-1]
        elif len(key) == 1:
            self.value += key

        self.text_entity.text = self.value or self.placeholder

    def update(self):
        self.text_entity.world_position = self.world_position + (0, 0, -0.01)
        if self.hovered and mouse.left and not self.active:
            self.active = True
        elif not self.hovered and mouse.left:
            self.active = False

        # Cursor blink logic
        if self.active and time.time() % 1 < 0.5:
            self.text_entity.text = self.value + '|'
        elif self.active:
            self.text_entity.text = self.value
        elif not self.value:
            self.text_entity.text = self.placeholder

    def on_destroy(self):
        destroy(self.text_entity)
