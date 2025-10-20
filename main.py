import sys
from parser import parse
import image
import palettefactory
import fractalfactory
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate fractal images')
    parser.add_argument('fractal_file', nargs='?', help='Path to fractal configuration file')
    parser.add_argument('palette', nargs='?', default='default', help='Palette name (default: default)')
    parser.add_argument('--no-gui', '--headless', action='store_true', 
                       help='Generate fractal without showing GUI window')
    
    args = parser.parse_args()

    # Handle the case where no fractal file is provided (use default)
    if args.fractal_file is None:
        config = {'name': 'phoenix', 'pixels': 512, 'type': 'phoenix', 'iterations': 256, 'centerx': -0.7466, 'centery': 0.1069, 'axislength': 0.001, 'preal': -0.3, 'pimag': 0.1, 'creal': -0.8, 'cimag': 0.78}
        name = 'Default'
    else:
        name, config = parse(args.fractal_file)
    
    # Create palette and fractal objects
    pfactory = palettefactory.PaletteFactory()
    palette = pfactory.make(config['iterations'], args.palette)

    ffactory = fractalfactory.FractalFactory()
    fractal = ffactory.make(config['type'], config['iterations'], config)

    # Generate the fractal image
    image.makeImage(config, fractal, palette, headless=args.no_gui)

if __name__ == "__main__":
    main()