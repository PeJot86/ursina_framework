from engine.plugins.decorator import plugin_registry

def load_plugins():
    print(f"[PLUGINS] Ładowanie {len(plugin_registry)} pluginów...")
    return plugin_registry