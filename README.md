#  Y'Urscene - Ursina Game Framework

A modular game framework built with [Ursina Engine](https://www.ursinaengine.org/) in Python. Designed for rapid prototyping and clean separation between scenes, plugins, and core systems.

## Features

* ✅ Scene Manager
* 🔌 Plugin System (e.g., DebugOverlay)
* 🎮 Simple Game Structure (`GameApp`, `Scene`, `Plugin` base classes)
* 🧱 Extendable UI and game logic

## Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/your_username/ursina-framework.git
   cd ursina-framework
   ```

2. **Create virtual environment** (optional but recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python main.py
   ```

## Folder Structure

```
ursina_framework/
├── engine/             # Core systems: app, scene manager, plugin loader
├── game/
│   └── scenes/         # Game-specific scenes (menu, gameplay, etc.)
├── plugins/            # Plugins (e.g. DebugOverlay)
├── assets/             # Textures, models, sounds
├── main.py             # Entry point
└── requirements.txt    # Python dependencies
```

## License

MIT
