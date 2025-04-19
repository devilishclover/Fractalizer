from colour import Color

class Palette:
    def __init__(self, num_colors):
        if type(self) is Palette:
            raise NotImplementedError("Palette is an abstract class and must be extended")
        self.num_colors = num_colors

    def get_color(self, n):
        raise NotImplementedError("Concrete subclass of Palette must override get_color()")

    def __len__(self):
        return self.num_colors
    
class RainbowColors(Palette):
    def __init__(self, n):
        super().__init__(n)
        self.colors = list(Color("red").range_to(Color("violet"), n))

    def get_color(self, n):
        n = n % self.num_colors
        return self.colors[n].get_hex_l()

class FireColors(Palette):
    def __init__(self, n):
        super().__init__(n)
        self.colors = []
        self.colors.extend(Color("black").range_to(Color("red"), n // 3))
        self.colors.extend(Color("red").range_to(Color("yellow"), n // 3))
        self.colors.extend(Color("yellow").range_to(Color("white"), n - 2 * (n // 3)))

    def get_color(self, n):
        n = n % self.num_colors
        return self.colors[n].get_hex_l()

class BlueGreen(Palette):
    def __init__(self, n):
        super().__init__(n)
        self.colors = list(Color("blue").range_to(Color("green"), n))

    def get_color(self, n):
        n = n % self.num_colors
        return self.colors[n].get_hex_l()

class RepeatingStripes(Palette):
    def __init__(self, n):
        super().__init__(n)
        self.color1 = "#000000"
        self.color2 = "#FFFFFF"
        self.stripe_width = 16 

    def get_color(self, n):
        if (n // self.stripe_width) % 2 == 0:
            return self.color1
        else:
            return self.color2

class ChristmasColors(Palette):
    def __init__(self, n):
        super().__init__(n)
        self.colors = []
        self.colors.extend(Color("#FF0000").range_to(Color("#006400"), n // 3))  # Red to Green
        self.colors.extend(Color("#006400").range_to(Color("#FFFFFF"), n // 3))  # Green to White
        self.colors.extend(Color("#FFFFFF").range_to(Color("#FFD700"), n - 2 * (n // 3)))  # White to Gold

    def get_color(self, n):
        n = n % self.num_colors
        return self.colors[n].get_hex_l()
