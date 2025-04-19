import fractals

class FractalFactory:
    def __init__(self):
        self.fractal = None
    def make(self, name, max_iterations, config=None):
        if name == "mandelbrot":
            self.fractal = fractals.Mandelbrot(max_iterations)
        elif name == "mandelbrot3":
            self.fractal = fractals.Mandelbrot3(max_iterations)
        elif name == "mandelbrot4":
            self.fractal = fractals.Mandelbrot4(max_iterations)
        elif name == "mandelbrot5":
            self.fractal = fractals.Mandelbrot5(max_iterations)
        elif name == "phoenix":
            self.fractal = fractals.Phoenix(max_iterations, config)
        elif name == "burningship":
            self.fractal = fractals.BurningShip(max_iterations)
        elif name == "julia":
            self.fractal = fractals.Julia(max_iterations, config)
        else:
            raise ValueError(f"Unknown fractal name: {name}")
        return self.fractal
