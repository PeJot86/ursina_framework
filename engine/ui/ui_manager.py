from ursina import destroy

class UIManager:
    def __init__(self):
        self.windows = []

    def open_window(self, window, exclusive=True):
        if exclusive:
            self.close_all()
        if window not in self.windows and not getattr(window, '_destroyed', False):
            self.windows.append(window)
        window.enabled = True
        window.visible = True

    def close_window(self, window):
        if window in self.windows:
            destroy(window)
            self.windows.remove(window)

    def close_all(self):
        for window in self.windows:
            if window and not window._destroyed:
                destroy(window)
        self.windows.clear()

    def toggle_window(self, window):
        if window in self.windows:
            self.close_window(window)
        else:
            self.open_window(window, exclusive=False)

# --- singleton instance ---
ui_manager = UIManager()
