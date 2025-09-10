# Sakura Tree Generator

A simple Python script that uses the `turtle` module to draw a stylized Sakura (cherry blossom) tree with randomized branching and pink blossoms.

## Features
- Randomized branching for natural variation
- Brown branches with occasional pink blossoms
- Fast rendering using disabled animation and a single final screen update

## Requirements
- Python 3.8+
- Standard library `turtle` (pre-installed with Python)

## Usage
```bash
python sakura.py
```

If you're on Windows and double-clicking the file doesn't work, run it from a terminal in the same directory.

## How it works
- Recursively draws branches with decreasing length
- Randomly changes color between brown and pink for blossoms when branch length is small
- Uses `screen.tracer(0, 0)` and `screen.update()` for efficient drawing

## License
MIT
