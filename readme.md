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
    # Using Poetry (recommended)
    poetry run python main.py data/m-basic.frac --no-gui
    
    # Or directly with Python
    python main.py data/m-basic.frac --no-gui
    
    # You can also use --headless instead of --no-gui
    poetry run python main.py data/m-basic.frac --headless
    ```
    
    In headless mode, the fractal is generated and saved to the `/output` folder without displaying a GUI window. This is useful for batch processing or running on systems without a display.

The configuration files are found in the /data folder. Files starting with m- are Mandelbrot files and files starting with p- are Phoenix files, files starting with bs- are burning ship files, and files starting with j- are julia files.

## Available Palettes

The following color palettes can be specified as the second argument:

* **default** - Standard rainbow colors
* **rainbow** - rainbow spectrum
* **fire** - flames 🔥🔥🔥🔥🔥
* **bluegreen** - blue and green spectrum
* **stripes** - Black and white
* **christmas** - Christmas colors

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

## Common Errors

| Error | Message | Solution |
|-------|---------|----------|
| **File Not Found** | `FileNotFoundError: [Errno 2] No such file or directory` | Verify that your file paths are correct |
| **Incorrect Fractal Type** | `Warning! incompatible fractal type detected: 'mandelbrot'` | Make sure you're using the correct program for the fractal type |
| **Invalid Palette** | `ValueError: Unknown palette name: [name]` | Use one of the valid palette names listed above |
