import palettes

class PaletteFactory:
    def __init__(self):
        self.palette = None
    def make(self, num_colors, name="rainbowcolors"):
        if name == "default":
            self.palette = palettes.RainbowColors(num_colors)
        elif name == "rainbow":
            self.palette = palettes.RainbowColors(num_colors)
        elif name == "fire":
            self.palette = palettes.FireColors(num_colors)
        elif name == "bluegreen":
            self.palette = palettes.BlueGreen(num_colors)
        elif name == "stripes":
            self.palette = palettes.RepeatingStripes(num_colors)
        elif name == "christmas":
            self.palette = palettes.ChristmasColors(num_colors)
        else:
            raise ValueError(f"Unknown palette name: {name}")
        return self.palette