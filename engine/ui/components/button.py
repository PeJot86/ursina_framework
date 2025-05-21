from ursina import Button, Func, color

class UIButton(Button):
    def __init__(self, text='OK', parent=None, scale=(0.3, 0.1), position=(0, 0), on_click=None, **kwargs):
        super().__init__(
            text=text,
            parent=parent,
            scale=scale,
            position=position,
            color=color.gray,
            highlight_color=color.azure,
            pressed_color=color.white,
            **kwargs 
        )

        if on_click:
            self.on_click = Func(on_click)

    def on_destroy(self):
        pass  # Button sam niszczy swoje komponenty
