plugin_registry = []

def plugin(cls):
    plugin_registry.append(cls())
    return cls
