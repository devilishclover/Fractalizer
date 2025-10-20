"""
Main animation orchestration for fractal animations.
"""

import sys
import copy
from pathlib import Path
from .interpolator import LinearInterpolator
from .video_renderer import VideoRenderer


class FractalAnimator:
    """Orchestrates the entire fractal animation process."""
    
    def __init__(self, base_config, fractal_factory, palette, animation_config):
        """
        Initialize fractal animator.
        
        Args:
            base_config (dict): Base fractal configuration
            fractal_factory: Factory for creating fractal instances
            palette: Color palette for rendering
            animation_config: Animation configuration parameters
        """
        self.base_config = base_config.copy()
        self.fractal_factory = fractal_factory
        self.palette = palette
        self.animation_config = animation_config
        self.interpolator = LinearInterpolator()  # Default interpolator
        self.video_renderer = VideoRenderer()
        
        # Validate animation config against fractal config
        self.animation_config.validate_against_config(self.base_config)
        
    def set_interpolator(self, interpolator):
        """
        Set custom interpolation strategy.
        
        Args:
            interpolator: Interpolator instance to use
        """
        self.interpolator = interpolator
        
    def set_video_settings(self, fps=30, quality='high'):
        """
        Configure video output settings.
        
        Args:
            fps (int): Frames per second
            quality (str): Video quality setting
        """
        self.video_renderer = VideoRenderer(fps=fps, quality=quality)
        
    def generate_animation(self):
        """
        Main animation generation pipeline.
        
        Returns:
            str: Path to generated video file, or None if failed
        """
        print(f"Starting animation generation: {self.animation_config}", file=sys.stderr)
        
        try:
            # 1. Generate interpolated values
            values = self.interpolator.generate_values(
                self.animation_config.start_value,
                self.animation_config.end_value,
                self.animation_config.frames
            )
            
            print(f"Generated {len(values)} interpolated values", file=sys.stderr)
            
            # 2. Create temporary directory
            temp_dir = Path('./temp')
            temp_dir.mkdir(exist_ok=True)
            
            # 3. Generate frame images
            temp_files = []
            for i, value in enumerate(values):
                frame_config = self._create_frame_config(value)
                frame_path = temp_dir / f"frame_{i:04d}.png"
                
                # Import here to avoid circular imports
                from image import makeImage
                
                # Create fractal for this frame
                fractal = self.fractal_factory.make(
                    frame_config['type'], 
                    frame_config['iterations'], 
                    frame_config
                )
                
                # Generate frame image
                print(f"Generating frame {i+1}/{len(values)} "
                      f"({self.animation_config.parameter}={value:.6f})", 
                      end="\r", file=sys.stderr)
                      
                makeImage(frame_config, fractal, self.palette, 
                         headless=True, save_path=str(frame_path))
                         
                temp_files.append(str(frame_path))
                
            print(f"\nGenerated {len(temp_files)} frame images", file=sys.stderr)
            
            # 4. Compile to video
            video_path = f"./output/{self.animation_config.output_name}.mp4"
            success = self.video_renderer.compile_to_mp4(temp_files, video_path)
            
            # 5. Cleanup temporary files
            self.video_renderer.cleanup_temp_files(temp_files)
            
            if success:
                print(f"Animation complete: {video_path}", file=sys.stderr)
                return video_path
            else:
                print("Animation failed during video compilation", file=sys.stderr)
                return None
                
        except Exception as e:
            print(f"Animation generation failed: {e}", file=sys.stderr)
            return None
            
    def _create_frame_config(self, parameter_value):
        """
        Create configuration for a single animation frame.
        
        Args:
            parameter_value (float): Value for the animated parameter
            
        Returns:
            dict: Modified configuration for this frame
        """
        frame_config = copy.deepcopy(self.base_config)
        frame_config[self.animation_config.parameter] = parameter_value
        return frame_config
        
    def preview_values(self):
        """
        Preview the interpolated values without generating images.
        
        Returns:
            list: List of interpolated values
        """
        values = self.interpolator.generate_values(
            self.animation_config.start_value,
            self.animation_config.end_value,
            self.animation_config.frames
        )
        
        print(f"Animation preview for {self.animation_config.parameter}:")
        print(f"  Frames: {self.animation_config.frames}")
        print(f"  Range: {self.animation_config.start_value} → {self.animation_config.end_value}")
        print(f"  Interpolator: {self.interpolator.__class__.__name__}")
        print(f"  Sample values: {values[:5]}{'...' if len(values) > 5 else ''}")
        
        return values