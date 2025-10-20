import sys
from parser import parse
import image
import palettefactory
import fractalfactory
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate fractal images and animations')
    parser.add_argument('fractal_file', nargs='?', help='Path to fractal configuration file')
    parser.add_argument('palette', nargs='?', default='default', help='Palette name (default: default)')
    parser.add_argument('--no-gui', '--headless', action='store_true', 
                       help='Generate fractal without showing GUI window')
    
    # Animation arguments group
    animation_group = parser.add_argument_group('animation', 'Animation generation options')
    animation_group.add_argument('--animate', action='store_true',
                               help='Generate animation instead of single image')
    animation_group.add_argument('--frames', type=int, default=60,
                               help='Number of frames in animation (default: 60)')
    animation_group.add_argument('--parameter', 
                               choices=['centerx', 'centery', 'axislength', 'creal', 'cimag', 'preal', 'pimag'],
                               help='Parameter to animate')
    animation_group.add_argument('--start', type=float,
                               help='Starting value for animated parameter')
    animation_group.add_argument('--end', type=float,
                               help='Ending value for animated parameter')
    animation_group.add_argument('--output', default='fractal_animation',
                               help='Output name for animation (default: fractal_animation)')
    animation_group.add_argument('--fps', type=int, default=30,
                               help='Frames per second for video output (default: 30)')
    animation_group.add_argument('--interpolation', 
                               choices=['linear', 'ease-in-out', 'sine-wave', 'back-and-forth'],
                               default='linear',
                               help='Interpolation method (default: linear)')
    animation_group.add_argument('--quality',
                               choices=['low', 'medium', 'high', 'lossless'],
                               default='high',
                               help='Video quality (default: high)')
    
    args = parser.parse_args()
    
    # Validate animation arguments
    if args.animate:
        if not all([args.parameter, args.start is not None, args.end is not None]):
            parser.error("Animation mode requires --parameter, --start, and --end arguments")
        if args.fractal_file is None:
            parser.error("Animation mode requires a fractal configuration file")

    # Handle the case where no fractal file is provided (use default)
    if args.fractal_file is None:
        config = {'name': 'phoenix', 'pixels': 512, 'type': 'phoenix', 'iterations': 256, 'centerx': -0.7466, 'centery': 0.1069, 'axislength': 0.001, 'preal': -0.3, 'pimag': 0.1, 'creal': -0.8, 'cimag': 0.78}
        name = 'Default'
    else:
        name, config = parse(args.fractal_file)
    
    # Create palette and fractal factory
    pfactory = palettefactory.PaletteFactory()
    palette = pfactory.make(config['iterations'], args.palette)

    ffactory = fractalfactory.FractalFactory()
    
    if args.animate:
        # Animation mode
        try:
            from animation import FractalAnimator, AnimationConfig
            from animation.interpolator import (LinearInterpolator, EaseInOutInterpolator, 
                                              SineWaveInterpolator, BackAndForthInterpolator)
        except ImportError:
            print("Animation dependencies not installed. Run: poetry install --with animation", 
                  file=sys.stderr)
            sys.exit(1)
        
        # Create animation configuration
        animation_config = AnimationConfig(
            frames=args.frames,
            parameter=args.parameter,
            start_value=args.start,
            end_value=args.end,
            output_name=args.output
        )
        
        # Create animator
        animator = FractalAnimator(config, ffactory, palette, animation_config)
        
        # Set interpolation method
        interpolator_map = {
            'linear': LinearInterpolator(),
            'ease-in-out': EaseInOutInterpolator(),
            'sine-wave': SineWaveInterpolator(),
            'back-and-forth': BackAndForthInterpolator()
        }
        animator.set_interpolator(interpolator_map[args.interpolation])
        
        # Set video settings
        animator.set_video_settings(fps=args.fps, quality=args.quality)
        
        # Generate animation
        result = animator.generate_animation()
        if result is None:
            sys.exit(1)
    else:
        # Single image mode (existing functionality)
        fractal = ffactory.make(config['type'], config['iterations'], config)
        image.makeImage(config, fractal, palette, headless=args.no_gui)

if __name__ == "__main__":
    main()