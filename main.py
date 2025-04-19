import sys
from parser import parse
import image
import palettefactory
import fractalfactory

if __name__ == "__main__":
    if len(sys.argv) == 1:
        config = {'name': 'phoenix', 'pixels': 512, 'type': 'phoenix', 'iterations': 256, 'centerx': -0.7466, 'centery': 0.1069, 'axislength': 0.001, 'preal': -0.3, 'pimag': 0.1, 'creal': -0.8, 'cimag': 0.78}
        name = 'Default'
        pfactory = palettefactory.PaletteFactory()
        palette = pfactory.make(config['iterations'], 'default')

        ffactory = fractalfactory.FractalFactory()
        fractal = ffactory.make(config['type'], config['iterations'], config)


        image.makeImage(config, fractal, palette)

    elif len(sys.argv) == 2:
        fractal_file = sys.argv[1]

        name, config = parse(fractal_file)

        pfactory = palettefactory.PaletteFactory()
        palette = pfactory.make(config['iterations'], 'default')

        ffactory = fractalfactory.FractalFactory()
        fractal = ffactory.make(config['type'], config['iterations'], config)

        image.makeImage(config, fractal, palette)

    elif len(sys.argv) == 3:
        palette_name = sys.argv[2]
        fractal_file = sys.argv[1]

        name, config = parse(fractal_file)

        pfactory = palettefactory.PaletteFactory()
        palette = pfactory.make(config['iterations'], palette_name)

        ffactory = fractalfactory.FractalFactory()
        fractal = ffactory.make(config['type'], config['iterations'], config)

        image.makeImage(config, fractal, palette)

    else:
        print("incorrect usage see manual")
        sys.exit(1)