# Fractalizer

## Running the Program

### Requirements:

#### System Requirements:
* Python 3.8.1 or higher
* tkinter GUI support (usually included with Python, but may need to be installed separately on some Linux distributions)

**Installing tkinter on Linux (if needed):**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora/RHEL/CentOS
sudo dnf install tkinter
# or
sudo yum install tkinter

# Arch Linux
sudo pacman -S tk
```

#### Python Dependencies:
The easiest way to install all required Python modules is using Poetry:

```bash
# Install dependencies
poetry install

# Run the program using Poetry
poetry run python main.py
```

**Alternative manual installation:**
```bash
pip install colour
pip install pygame
```

To run the program, run main.py with the arguments you want to use.

1. **No arguments** - default Phoenix fractal configuration:
    ```bash
    # Using Poetry (recommended)
    poetry run python main.py
    
    # Or directly with Python
    python main.py
    ```

2. **With fractal configuration file** - Specify a fractal configuration file from the /data folder:
    ```bash
    # Using Poetry (recommended)  
    poetry run python main.py data/p-monkey-knife-fight.frac
    
    # Or directly with Python
    python main.py data/p-monkey-knife-fight.frac
    ```

3. **With fractal configuration and palette** - Specify both a configuration file and a color palette:
    ```bash
    # Using Poetry (recommended)
    poetry run python main.py data/m-basic.frac fire
    
    # Or directly with Python
    python main.py data/m-basic.frac fire
    ```

4. **Headless mode (no GUI window)** - Generate fractals without showing the GUI window:
    ```bash
    poetry run python main.py data/m-basic.frac --no-gui
    ```

5. **Animation mode** - Generate animated fractals:
    ```bash
    poetry run python main.py data/m-basic.frac fire --animate \
        --parameter axislength --start 4.0 --end 0.1 --frames 60
    ```

<details>
<summary><strong>Advanced Usage Options</strong></summary>

### Headless Mode Details

```bash
# Using Poetry (recommended)
poetry run python main.py data/m-basic.frac --no-gui

# Or directly with Python
python main.py data/m-basic.frac --no-gui

# You can also use --headless instead of --no-gui
poetry run python main.py data/m-basic.frac --headless
```

In headless mode, the fractal is generated and saved to the `/output` folder without displaying a GUI window. This is useful for batch processing or running on systems without a display.

### Animation Mode Details

Animation mode requires additional dependencies:
```bash
poetry install --with animation
```

See the Animation Features section below for detailed examples and parameters.

</details>

5. **Animation mode** - Generate animated fractals by interpolating parameter values:
    ```bash
    # Basic zoom animation
    poetry run python main.py data/m-basic.frac fire --animate \
        --parameter axislength --start 4.0 --end 0.1 --frames 60 --output zoom_animation
    
    # Smooth panning animation with ease-in-out
    poetry run python main.py data/j-basic.frac rainbow --animate \
        --parameter centerx --start -2.0 --end 2.0 --frames 120 \
        --interpolation ease-in-out --fps 30 --output julia_pan
    
    # Complex parameter animation (Julia set constant)
    poetry run python main.py data/j-basic.frac christmas --animate \
        --parameter creal --start -1.0 --end 1.0 --frames 90 \
        --interpolation sine-wave --quality high --output julia_morph
    ```
    
    Animation mode requires the optional animation dependencies:
    ```bash
    poetry install --with animation
    ```

The configuration files are found in the /data folder. Files starting with m- are Mandelbrot files and files starting with p- are Phoenix files, files starting with bs- are burning ship files, and files starting with j- are julia files.

## Available Palettes

The following color palettes can be specified as the second argument:

* **default** - Standard rainbow colors
* **rainbow** - rainbow spectrum
* **fire** - flames 🔥🔥🔥🔥🔥
* **bluegreen** - blue and green spectrum
* **stripes** - Black and white
* **christmas** - Christmas colors

<details>
<summary><strong>Animation Features</strong></summary>

## Animation Parameters

When using `--animate`, you can animate the following parameters:

* **centerx** / **centery** - Pan across the fractal plane
* **axislength** - Zoom in or out of the fractal
* **creal** / **cimag** - Change Julia set constants (for Julia fractals)
* **preal** / **pimag** - Change Phoenix fractal constants (for Phoenix fractals)

## Interpolation Methods

Choose how values change between start and end:

* **linear** - Constant rate of change (default)
* **ease-in-out** - Smooth acceleration and deceleration
* **sine-wave** - Oscillating motion following a sine wave
* **back-and-forth** - Go from start to end and back to start

## Animation Examples

```bash
# Zoom animation with linear interpolation
poetry run python main.py data/m-basic.frac fire --animate \
    --parameter axislength --start 4.0 --end 0.1 --frames 60 \
    --output mandelbrot_zoom

# Smooth panning with ease-in-out
poetry run python main.py data/j-basic.frac rainbow --animate \
    --parameter centerx --start -2.0 --end 2.0 \
    --interpolation ease-in-out --fps 30 --output julia_pan

# Julia constant animation with back-and-forth motion  
poetry run python main.py data/j-basic.frac christmas --animate \
    --parameter creal --start -1.5 --end 0.5 \
    --interpolation back-and-forth --frames 120 --output julia_morph

# High quality sine wave zoom
poetry run python main.py data/m-basic.frac fire --animate \
    --parameter axislength --start 2.0 --end 0.01 \
    --interpolation sine-wave --quality lossless --fps 60
```

## Animation Requirements

To use animation features, install the animation dependencies:

```bash
# Install animation dependencies
poetry install --with animation

# Or manually install required packages
pip install opencv-python numpy pillow imageio
```

**Note:** FFmpeg is recommended for best video quality but the system will fall back to Python libraries if not available.

</details>

## Program Execution

When the program runs successfully:
1. A window opens showing the fractal generation
2. progress percentage and the name of the fractal are shown in the console
3. the fractal finishes and when the window is closed the file is saved

### Example Output:

**GUI Mode:**
```
Rendering phoenix fractal
[100% =================================]
Done in 2.430 seconds!
Close the image window to exit the program
```

**Headless Mode:**
```
Rendering mandelbrot fractal
[100% =================================]
Done in 1.911 seconds!
Image saved to ./output/mandelbrot.png
```

**Animation Mode:**
```
Starting animation generation: AnimationConfig(frames=60, parameter='axislength', range=4.0→0.1, output='zoom')
Generated 60 interpolated values
Generating frame 60/60 (axislength=0.100000)
Generated 60 frame images
Video successfully created: ./output/zoom.mp4
Cleanup complete: 60 files removed
Animation complete: ./output/zoom.mp4
```

<details>
<summary><strong>Troubleshooting & Common Errors</strong></summary>

| Error | Message | Solution |
|-------|---------|----------|
| **File Not Found** | `FileNotFoundError: [Errno 2] No such file or directory` | Verify that your file paths are correct |
| **Incorrect Fractal Type** | `Warning! incompatible fractal type detected: 'mandelbrot'` | Make sure you're using the correct program for the fractal type |
| **Invalid Palette** | `ValueError: Unknown palette name: [name]` | Use one of the valid palette names listed above |
| **Animation Dependencies** | `ImportError: Animation dependencies not installed` | Run `poetry install --with animation` |
| **Video Creation Failed** | `All video creation methods failed` | Install ffmpeg, or ensure opencv-python/imageio are available |
| **Invalid Parameter** | `ValueError: Invalid parameter 'xyz'` | Use valid parameters: centerx, centery, axislength, creal, cimag, preal, pimag |

### Performance Tips

- Use `--no-gui` for faster generation when you don't need to see the preview
- Lower frame counts for testing animations before final render
- Use 'low' quality setting for preview animations
- Higher iteration counts create more detailed fractals but take longer to render

</details>
