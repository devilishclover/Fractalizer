"""
Animation configuration management for fractal animations.
"""


class AnimationConfig:
    """Encapsulates animation parameters and validation."""
    
    VALID_PARAMETERS = {
        'centerx', 'centery', 'axislength', 
        'creal', 'cimag', 'preal', 'pimag'
    }
    
    def __init__(self, frames, parameter, start_value, end_value, output_name):
        """
        Initialize animation configuration.
        
        Args:
            frames (int): Number of frames to generate
            parameter (str): Parameter name to animate
            start_value (float): Starting value for the parameter
            end_value (float): Ending value for the parameter  
            output_name (str): Base name for output files
        """
        self.frames = frames
        self.parameter = parameter
        self.start_value = start_value
        self.end_value = end_value
        self.output_name = output_name
        self.validate()
        
    def validate(self):
        """Validate animation configuration parameters."""
        if self.frames < 2:
            raise ValueError("Animation must have at least 2 frames")
            
        if self.frames > 10000:
            raise ValueError("Frame count too high (max 10000 for safety)")
            
        if self.parameter not in self.VALID_PARAMETERS:
            raise ValueError(f"Invalid parameter '{self.parameter}'. "
                           f"Valid parameters: {', '.join(sorted(self.VALID_PARAMETERS))}")
                           
        if not isinstance(self.start_value, (int, float)):
            raise ValueError("Start value must be numeric")
            
        if not isinstance(self.end_value, (int, float)):
            raise ValueError("End value must be numeric")
            
        if not self.output_name or not isinstance(self.output_name, str):
            raise ValueError("Output name must be a non-empty string")
            
    def validate_against_config(self, fractal_config):
        """
        Validate that the parameter exists in the given fractal configuration.
        
        Args:
            fractal_config (dict): Fractal configuration dictionary
        """
        if self.parameter not in fractal_config:
            raise ValueError(f"Parameter '{self.parameter}' not found in fractal configuration. "
                           f"Available parameters: {', '.join(sorted(fractal_config.keys()))}")
                           
    def __str__(self):
        return (f"AnimationConfig(frames={self.frames}, parameter='{self.parameter}', "
                f"range={self.start_value}→{self.end_value}, output='{self.output_name}')")