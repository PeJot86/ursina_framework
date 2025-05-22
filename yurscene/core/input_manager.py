from ursina import held_keys

class InputManager:
    def __init__(self):
        self._bindings = {}
        self._pressed_flags = set()

    def bind(self, key_combo: str, action: callable):
        """Przypisz akcję do klawisza lub kombinacji np. 'ctrl+z'"""
        normalized = self._normalize_combo(key_combo)
        self._bindings[normalized] = action

    def unbind(self, key_combo: str):
        normalized = self._normalize_combo(key_combo)
        self._bindings.pop(normalized, None)
        self._pressed_flags.discard(normalized)

    def clear(self):
        self._bindings.clear()
        self._pressed_flags.clear()

    def handle(self, key: str):
        """Wywołuje skrót (jeśli pasuje) — tylko raz"""
        modifiers = []
        if held_keys['control']: modifiers.append('ctrl')
        if held_keys['shift']: modifiers.append('shift')
        if held_keys['alt']: modifiers.append('alt')

        combo = '+'.join(modifiers + [key])
        normalized = self._normalize_combo(combo)

        if normalized in self._bindings and normalized not in self._pressed_flags:
            self._bindings[normalized]()
            self._pressed_flags.add(normalized)

    def release(self, key: str):
        """Odblokowuje skrót po puszczeniu przycisku"""
        to_remove = [combo for combo in self._pressed_flags if combo.endswith(f'+{key}') or combo == key]
        for combo in to_remove:
            self._pressed_flags.discard(combo)

    def update(self):
        """Obsługa skrótów także przez held_keys (na wypadek braku input())"""
        for combo, action in self._bindings.items():
            parts = combo.split('+')
            modifiers = {'ctrl': 'control', 'shift': 'shift', 'alt': 'alt'}
            mods_ok = all(held_keys.get(modifiers[m], 0) for m in parts[:-1] if m in modifiers)
            key = parts[-1]
            if mods_ok and held_keys.get(key, 0) and combo not in self._pressed_flags:
                action()
                self._pressed_flags.add(combo)

        # Usuwanie nieaktywnych
        to_remove = []
        for combo in self._pressed_flags:
            parts = combo.split('+')
            modifiers = {'ctrl': 'control', 'shift': 'shift', 'alt': 'alt'}
            mods_ok = all(held_keys.get(modifiers[m], 0) for m in parts[:-1] if m in modifiers)
            key = parts[-1]
            if not (mods_ok and held_keys.get(key, 0)):
                to_remove.append(combo)
        for combo in to_remove:
            self._pressed_flags.remove(combo)

    def _normalize_combo(self, combo: str) -> str:
        parts = combo.lower().split('+')
        modifiers = sorted(p for p in parts if p in ['ctrl', 'shift', 'alt'])
        key = next((p for p in parts if p not in modifiers), '')
        return '+'.join(modifiers + [key]) if key else ''
