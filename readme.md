# Fractalizer

## Running the Program

### Requrements:

* The following modules must be installed:
    ```
    pip install colour
    pip install pygame
    ```

To run the program, run main.py with the arguments you want to use.

1. **No arguments** - default Phoenix fractal configuration:
    ```
    $ python src/main.py
    ```

2. **With fractal configuration file** - Specify a fractal configuration file from the /data folder:
    ```
    $ python src/main.py data/p-monkey-knife-fight.frac
    ```

3. **With fractal configuration and palette** - Specify both a configuration file and a color palette:
    ```
    $ python src/main.py data/mandelbrot.frac fire
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

## Program Execution

When the program runs successfully:
1. A window opens showing the fractal generation
2. progress percentage and the name of the fractal are shown in the console
3. the fractal finishes and when the window is closed the file is saved

### Example Output:
```
Rendering p-shrimp-cocktail fractal
[100% =================================]
Done in 2.489 seconds!
Saved image to file p-shrimp-cocktail.png
Close the image window to exit the program
```

## Common Errors

| Error | Message | Solution |
|-------|---------|----------|
| **File Not Found** | `FileNotFoundError: [Errno 2] No such file or directory` | Verify that your file paths are correct |
| **Incorrect Fractal Type** | `Warning! incompatible fractal type detected: 'mandelbrot'` | Make sure you're using the correct program for the fractal type |
| **Invalid Palette** | `ValueError: Unknown palette name: [name]` | Use one of the valid palette names listed above |
