from ursina import *

class UIPanel(Entity):
    def __init__(self, parent=None, scale=(0.5, 0.3), color=color.black66, padding=0.02, corner_radius=0.02, **kwargs):
        super().__init__(
            parent=parent,
            model='quad',
            scale=scale,
            color=color,
            texture=None,
            **kwargs  # ← nie podajemy shader
        )

        self.padding = padding
        self.corner_radius = corner_radius
        self.children_container = Entity(parent=self)

