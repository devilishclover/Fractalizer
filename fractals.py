class Fractal:
    def __init__(self, frac):
        if type(self) is Fractal:
            raise NotImplementedError("Fractal is an abstract class and must be extended")

    def count(self, z):
        raise NotImplementedError("Concrete subclass of Fractal must implement count()")
    
class Mandelbrot(Fractal):
    def __init__(self, max_iterations):
        super().__init__(self)
        self.max_iterations = max_iterations

    def count(self, c):
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = z * z + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations
    
class Mandelbrot3(Fractal):
    def __init__(self, max_iterations):
        super().__init__(self)
        self.max_iterations = max_iterations

    def count(self, c):
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = z * z * z + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations
    
class Mandelbrot4(Fractal):
    def __init__(self, max_iterations):
        super().__init__(self)
        self.max_iterations = max_iterations

    def count(self, c):
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = z * z * z * z + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations
    
class Mandelbrot5(Fractal):
    def __init__(self, max_iterations):
        super().__init__(self)
        self.max_iterations = max_iterations

    def count(self, c):
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = z * z * z * z * z + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations
    
class Phoenix(Fractal):
    def __init__(self, max_iterations, config):
        super().__init__(self)
        self.max_iterations = max_iterations
        self.config = config

    def count(self, z):
        c = complex(self.config['creal'], self.config['cimag'])
        phoenix = complex(self.config['preal'], self.config['pimag'])
        zPrev = 0 
        for i in range(self.max_iterations):
            zSave = z
            z = z * z + c + (phoenix * zPrev)
            zPrev = zSave
            if abs(z) > 2:
                return i
        return self.max_iterations
    
class BurningShip(Fractal):
    def __init__(self, max_iterations):
        super().__init__(self)
        self.max_iterations = max_iterations
    
    def count(self, c):
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = complex(abs(z.real), abs(z.imag))**2 + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations
    
class Julia(Fractal):
    def __init__(self, max_iterations, config):
        super().__init__(self)
        self.max_iterations = max_iterations
        self.config = config
        
    def count(self, z):
        c = complex(self.config['creal'], self.config['cimag'])
        for iteration in range(self.max_iterations):
            z = z * z + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations
