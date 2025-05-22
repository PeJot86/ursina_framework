from ursina import Entity, Text, Button, color, destroy, camera

class UIWindow(Entity):
    def __init__(self, title='Okno', size=(0.6, 0.5), position=(0, 0), closable=True, **kwargs):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color.white66,
            scale=size,
            position=position,
            z=-0.9,
            **kwargs
        )

        # ✅ Nagłówek jako child (nie camera.ui!)
        self.title_text = Text(
            text=title,
            parent=self,                   
            origin=(0, 0),
            y=self.scale_y / 2 + 0.05,      # przesunięcie do góry
            z=-0.01,
            scale=3,
            color=color.black
        )

        # Przycisk zamknięcia
        if closable:
            self.close_button = Button(
                text='x',
                scale=(0.06, 0.06),
                parent=self,
                position=(self.scale_x / 2 - 0.05, self.scale_y / 2 - 0.05),
                color=color.red,
                text_color=color.white,
                z=-0.9
            )
            self.close_button.on_click = self.close


    def close(self):
        print("[DEBUG] Zamykam UIWindow")
        destroy(self)




