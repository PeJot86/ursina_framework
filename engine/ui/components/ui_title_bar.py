from ursina import Entity, Text, Button, color, camera

class UITitleBar(Entity):
    def __init__(self, text="Y'Urscene Framework", scene_manager=None, show_menu_button=True, **kwargs):
        kwargs.setdefault('parent', camera.ui)
        kwargs.setdefault('z', -0.01)
        super().__init__(**kwargs)

        self.scene_manager = scene_manager


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
            parent=self,
            origin=(0, 0),
            y=0.42,
            z=0.01,
            scale=1,
            size=0.025,
            color=color.white
        )

        if show_menu_button:
            self.menu_button = Button(
                text="Menu",
                parent=self,
                scale=(0.15, 0.06),
                position=(-0.7, 0.42, 0.01),
                color=color.gray,
                text_color=color.white,
                on_click=self.go_to_menu
            )

    def go_to_menu(self):
        if self.scene_manager:
            self.scene_manager.set_scene("menu")
        else:
            print("[UITitleBar] Brak scene_manager!")
