from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
from time import time

SIZE = 512

def makeImage(config, fractal, palette, headless=False, save_path=None):  
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    If headless=True, generate image without GUI and save directly to file.
    If save_path is provided, save to that path instead of default location.
    """
    b4 = time()
    # Use the fractal configuration name if available, otherwise fall back to type
    name = config.get('name', config['type'])

    if "pixels" in config:
        SIZE = config['pixels']

    print("Rendering %s fractal" % name, file=sys.stderr)
    canvasSize = SIZE
    
    if headless:
        # In headless mode, create a hidden window
        window = Tk()
        window.withdraw()  # Hide the window
        tkPhotoImage = PhotoImage(width=SIZE, height=SIZE)
    else:
        # Normal GUI mode
        window = Tk()
        tkPhotoImage = PhotoImage(width=SIZE, height=SIZE)
        tk_Interface_PhotoImage_canvas_pixel_object = Canvas(window, width=SIZE, height=SIZE, bg='#000000')
        tk_Interface_PhotoImage_canvas_pixel_object.create_image((SIZE/2, SIZE/2), image=tkPhotoImage, state="normal")
        tk_Interface_PhotoImage_canvas_pixel_object.pack()

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.f
    minx = config['centerx'] - (config['axislength'] / 2.0)
    maxx = config['centerx'] + (config['axislength'] / 2.0)
    miny = config['centery'] - (config['axislength'] / 2.0)
    maxy = config['centery'] + (config['axislength'] / 2.0)

    # Calculate the size of each pixel
    pixelsize = abs(maxx - minx) / canvasSize

    # Loop backwards through rows to draw the fractal
    for row in range(canvasSize, 0, -1):
        pixelColors = []
        for col in range(canvasSize):
            # Calculate the coordinates in the complex plane
            x = minx + col * pixelsize
            y = miny + row * pixelsize

            pixelColors.append(palette.get_color(fractal.count(complex(x, y))))

        # Update the PhotoImage with the current row of pixels
        pixelRow = '{' + ' '.join(pixelColors) + '}'
        tkPhotoImage.put(pixelRow, to=(0, canvasSize - row))
        
        if not headless:
            window.update()  # Display the updated row of pixels (only in GUI mode)
            window.update_idletasks()

        # Print a status bar to the console
        completionPercentage = (canvasSize - row) / canvasSize
        print(f"[{completionPercentage:>4.0%}"
              + f'{" "}'
              + f"{'=' * int(34 * completionPercentage):<33}]",
              end="\r", file=sys.stderr)

    # Determine save path
    if save_path:
        output_path = save_path
    else:
        output_path = f"./output/{name}.png"
    
    tkPhotoImage.write(output_path)
        
    print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)
    
    if headless:
        print(f"Image saved to {output_path}", file=sys.stderr)
        window.destroy()  # Clean up the hidden window
    else:
        print("Close the image window to exit the program", file=sys.stderr)
        mainloop()
