# Alien Invasion Game

A classic space shooter game built with Python and Pygame. Defend your ship against waves of descending aliens in this action-packed arcade-style game.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Game](#running-the-game)
- [Game Controls](#game-controls)
- [Gameplay](#gameplay)
- [Project Structure](#project-structure)
- [Settings & Configuration](#settings--configuration)
- [Game Mechanics](#game-mechanics)
- [Scoring System](#scoring-system)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Support](#support)

## About the Project

Alien Invasion Game is a Python-based space shooter game where players control a ship at the bottom of the screen and must defend it from incoming alien fleets. The game features progressive difficulty levels, a scoring system, and multiple lives. This project demonstrates core game development concepts including sprite management, collision detection, event handling, and game state management.

**Project Status:** Active Development

## Features

- ✈️ **Player-controlled ship** with smooth left/right movement
- 👾 **Dynamic alien fleet** that moves horizontally and descends vertically
- 🔫 **Bullet system** with maximum bullet limit for balanced gameplay
- 💥 **Collision detection** for bullet-alien and alien-ship interactions
- 📊 **Real-time scoring system** with high score tracking
- 🎯 **Progressive difficulty** - Speed and points increase with each level
- ❤️ **Lives system** - Lose lives when aliens hit your ship
- 🎮 **Play button** - Easy game restart functionality
- 🌊 **Level progression** - Complete levels by destroying all aliens
- 📱 **Responsive UI** - Score, level, and remaining ships displayed

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python 3.4+)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MuhammadTahirHussain-Official/Alien-Invasion-Game-in-Python.git
   cd Alien-Invasion-Game-in-Python
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install pygame
   ```

4. **Prepare game assets**
   
   Create an `images` folder in the project directory:
   ```
   Alien-Invasion-Game-in-Python/
   ├── images/
   │   ├── alien2.bmp
   │   └── ship.bmp
   ├── alien_invasion.py
   ├── alien.py
   ├── ship.py
   ├── bullet.py
   └── ... (other files)
   ```
   
   **Note:** Add your game sprite images (`alien2.bmp` and `ship.bmp`) to the `images` folder.

### Running the Game

Execute the main game file:

```bash
python alien_invasion.py
```

The game window will open at 1280x720 resolution. Click the **PLAY** button to start!

## Game Controls

| Control | Action |
|---------|--------|
| `←` Left Arrow | Move ship left |
| `→` Right Arrow | Move ship right |
| `Space` | Fire bullets |
| `Q` | Quit game |
| `Mouse Click` (on PLAY button) | Start/Restart game |

## Gameplay

### Objective
Destroy all aliens in each wave before they reach the bottom of the screen.

### Game Flow
1. **Start Screen** - Click the green PLAY button to begin
2. **Active Level** - Aliens descend from the top, moving left and right
3. **Fleet Behavior** - Aliens move horizontally and drop lower when reaching screen edges
4. **Collision Detection** - Bullets destroy aliens; aliens destroy your ship
5. **Level Completion** - All aliens destroyed = next level with increased difficulty
6. **Game Over** - All ships destroyed = return to start screen

### Winning Conditions
- Destroy all alien waves to progress through levels
- Survive and accumulate the highest score possible
- Each level increases in difficulty

### Losing Conditions
- All 3 ships are destroyed by aliens reaching the bottom
- Game ends and score is compared to high score

## Project Structure

```
Alien-Invasion-Game-in-Python/
│
├── alien_invasion.py       # Main game class and event loop
├── alien.py                # Alien sprite class
├── ship.py                 # Player ship sprite class
├── bullet.py               # Bullet sprite class
├── button.py               # Play button UI class
├── settings.py             # Game configuration and settings
├── game_stats.py           # Game statistics tracking
├── scoreboard.py           # Score display and UI rendering
├── images/                 # Game assets folder
│   ├── alien2.bmp
│   └── ship.bmp
├── README.md               # This file
└── .gitignore              # Git ignore file
```

## Settings & Configuration

Game settings can be modified in `settings.py`:

```python
# Screen dimensions
self.screen_width = 1280
self.screen_height = 720

# Ship settings
self.ship_speed = 1.5         # Pixels per frame
self.ship_limit = 3           # Lives per game

# Bullet settings
self.bullet_speed = 1.5       # Pixels per frame
self.bullet_height = 15       # Pixels
self.bullet_width = 3         # Pixels
self.bullet_allowed = 20      # Max bullets on screen

# Alien settings
self.alien_speed = 1.0        # Pixels per frame
self.fleet_drop_speed = 10    # Vertical drop pixels

# Difficulty scaling
self.speedup_scale = 1.1      # Speed multiplier per level
self.score_scale = 1.5        # Points multiplier per level
self.alien_points = 50        # Base points per alien
```

### Adjusting Difficulty

Modify these values in `settings.py`:
- **Increase `speedup_scale`** → Faster difficulty progression
- **Increase `alien_speed`** → Faster alien movement
- **Decrease `bullet_allowed`** → Reduced firepower
- **Increase `alien_points`** → Higher scoring

## Game Mechanics

### Sprite System
- **Pygame Sprites** - All game objects inherit from `pygame.sprite.Sprite`
- **Sprite Groups** - Used for efficient batch operations and collision detection

### Collision Detection
- **Bullet-Alien** - Uses `pygame.sprite.groupcollide()` for accurate detection
- **Ship-Alien** - Uses `pygame.sprite.spritecollideany()` for single collision check

### Fleet Movement
- Aliens move horizontally at constant speed
- When reaching screen edges, entire fleet drops vertically and reverses direction
- `fleet_direction` alternates between 1 (right) and -1 (left)

### Screen Boundaries
- **Ship** - Constrained to screen width
- **Bullets** - Removed when leaving top of screen
- **Aliens** - Trigger game event when reaching bottom of screen

## Scoring System

| Action | Points |
|--------|--------|
| Destroy alien (Level 1) | 50 |
| Destroy alien (increases per level) | 50 × (1.5)^(level-1) |
| Complete level | Bonus applied to next level |
| High Score | Persists during session |

**Example:**
- Level 1: 50 points per alien
- Level 2: 75 points per alien
- Level 3: 112 points per alien
- Level 4: 168 points per alien

## Technologies Used

- **Python 3.7+** - Programming language
- **Pygame 2.0+** - Game development library
- **Object-Oriented Programming (OOP)** - Design pattern

### Key Libraries
- `pygame` - Graphics, sprite management, event handling
- `sys` - System operations (quit)
- `time` - Pause functionality

## Future Enhancements

- [ ] Add sound effects and background music
- [ ] Implement power-ups (shields, rapid fire, etc.)
- [ ] Add boss aliens with unique behaviors
- [ ] Create multiple difficulty presets (Easy, Medium, Hard)
- [ ] Add explosions and visual effects
- [ ] Implement pause functionality
- [ ] Add config file for easy settings adjustment
- [ ] Create settings menu in-game
- [ ] Add persistent high score storage (JSON/Database)
- [ ] Implement achievements/milestones
- [ ] Add mobile/touchscreen support
- [ ] Create level progression file system

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**
   ```bash
   git clone https://github.com/MuhammadTahirHussain-Official/Alien-Invasion-Game-in-Python.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes** and test thoroughly

4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request** with a clear description of changes

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use descriptive variable and function names
- Add comments for complex logic
- Keep methods focused and single-responsibility

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2026 Muhammad Tahir Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

For full license text, see [LICENSE](LICENSE) file.

## Author

**Muhammad Tahir Hussain**
- GitHub: [@MuhammadTahirHussain-Official](https://github.com/MuhammadTahirHussain-Official)
- This is my first game development project!

## Support

### Troubleshooting

**Issue:** "ModuleNotFoundError: No module named 'pygame'"
- **Solution:** Install pygame using `pip install pygame`

**Issue:** "FileNotFoundError: No such file or directory"
- **Solution:** Update image paths in `alien.py` and `ship.py` to match your local setup, or place images in the `images/` folder and update paths to use relative paths

**Issue:** Game window doesn't open
- **Solution:** Ensure pygame is properly installed and your system has display capabilities

**Issue:** Game runs slowly
- **Solution:** Close other applications; lower screen resolution in `settings.py`

### Getting Help

- Check existing issues on [GitHub Issues](https://github.com/MuhammadTahirHussain-Official/Alien-Invasion-Game-in-Python/issues)
- Create a new issue with detailed description and error messages
- Reference line numbers and file names when reporting bugs

### Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Official Docs](https://docs.python.org/3/)
- [Game Development Tutorials](https://www.pygame.org/wiki/tutorials)

---

**Enjoy the game! 🚀👾**

Last Updated: May 1, 2026
