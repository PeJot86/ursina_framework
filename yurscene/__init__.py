# Public API 
from .core.base_scene import BaseScene
from .core.scene_manager import SceneManager
from .core.app import GameApp
from .ui.components.ui_title_bar import UITitleBar
from .ui.ui_manager import ui_manager


# Opcjonalne: logo przy imporcie
def _print_logo():
    print("=" * 50)
    print("         Y'Urscene Framework — v0.1.0")
    print("         Build modular. Think structured.")
    print("         Author: godssoft.com")
    print("=" * 50)

_print_logo()