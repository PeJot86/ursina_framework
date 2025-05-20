from ursina import Entity

class UIRow(Entity):
    def __init__(self, parent=None, padding=0.05, **kwargs):
        super().__init__(parent=parent, **kwargs)
        self.padding = padding

    def add(self, child):
        child.parent = self
        self.children.append(child)
        self.reflow()

    def reflow(self):
        x = 0
        for child in self.children:
            child.x = x
            x += child.scale_x + self.padding


class UIColumn(Entity):
    def __init__(self, parent=None, padding=0.05, **kwargs):
        super().__init__(parent=parent, **kwargs)
        self.padding = padding

    def add(self, child):
        child.parent = self
        self.children.append(child)
        self.reflow()

    def reflow(self):
        y = 0
        for child in self.children:
            child.y = y
            y -= child.scale_y + self.padding
