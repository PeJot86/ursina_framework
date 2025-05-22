from ursina import color

class UITheme:
    button_color = color.azure
    button_hover = color.cyan
    button_pressed = color.lime
    text_color = color.white

    @classmethod
    def get(cls):
        return cls
