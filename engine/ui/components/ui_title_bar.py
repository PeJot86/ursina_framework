from ursina import Entity, Text, color, camera

class UITitleBar(Entity):
    def __init__(self, text="Y'Urscene Framework", **kwargs):
        kwargs.setdefault('parent', camera.ui)
        kwargs.setdefault('z', -0.01)
        super().__init__(**kwargs)

        self.bg = Entity(
            parent=self,
            model='quad',
            color=color.black33,
            scale=(1.6, 0.12),
            y=0.42,
            z=0
        )

        self.label = Text(
            text=text,
            parent=self,         # ⬅⬅⬅ nie self.bg
            origin=(0, 0),
            y=0.42,
            z=0.01,              # ⬅⬅⬅ bliżej niż pasek
            scale=1,
            size=0.025,
            color=color.white
        )


