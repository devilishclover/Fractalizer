"""
Interpolation strategies for generating smooth animation sequences.
"""

import math
from abc import ABC, abstractmethod


class Interpolator(ABC):
    """Abstract base class for different interpolation strategies."""
    
    @abstractmethod
    def generate_values(self, start, end, steps):
        """
        Generate a sequence of interpolated values.
        
        Args:
            start (float): Starting value
            end (float): Ending value
            steps (int): Number of steps to generate
            
        Returns:
            list: List of interpolated values
        """
        pass


class LinearInterpolator(Interpolator):
    """Linear interpolation between start and end values."""
    
    def generate_values(self, start, end, steps):
        """Generate linearly spaced values between start and end."""
        if steps < 2:
            return [start]
            
        step_size = (end - start) / (steps - 1)
        return [start + i * step_size for i in range(steps)]


class EaseInOutInterpolator(Interpolator):
    """Smooth easing interpolation with ease-in and ease-out."""
    
    def generate_values(self, start, end, steps):
        """Generate smoothly eased values using cosine interpolation."""
        if steps < 2:
            return [start]
            
        values = []
        for i in range(steps):
            # Normalize to 0-1 range
            t = i / (steps - 1)
            
            # Apply ease-in-out function (smoothstep)
            eased_t = t * t * (3.0 - 2.0 * t)
            
            # Interpolate between start and end
            value = start + (end - start) * eased_t
            values.append(value)
            
        return values


class SineWaveInterpolator(Interpolator):
    """Sine wave interpolation for oscillating animations."""
    
    def __init__(self, cycles=1):
        """
        Initialize sine wave interpolator.
        
        Args:
            cycles (float): Number of complete sine wave cycles
        """
        self.cycles = cycles
    
    def generate_values(self, start, end, steps):
        """Generate sine wave oscillation between start and end."""
        if steps < 2:
            return [start]
            
        values = []
        amplitude = (end - start) / 2
        center = (start + end) / 2
        
        for i in range(steps):
            # Normalize to 0-1 range
            t = i / (steps - 1)
            
            # Apply sine wave
            angle = 2 * math.pi * self.cycles * t
            sine_value = math.sin(angle)
            
            # Scale and offset
            value = center + amplitude * sine_value
            values.append(value)
            
        return values


class BackAndForthInterpolator(Interpolator):
    """Interpolator that goes from start to end and back to start."""
    
    def generate_values(self, start, end, steps):
        """Generate values that go to end and return to start."""
        if steps < 2:
            return [start]
        
        # First half: start to end
        # Second half: end to start
        half_steps = steps // 2
        remainder = steps % 2
        
        # Generate first half
        first_half = LinearInterpolator().generate_values(start, end, half_steps + remainder)
        
        # Generate second half (reverse, excluding the end point to avoid duplication)
        second_half = LinearInterpolator().generate_values(end, start, half_steps + 1)[1:]
        
        return first_half + second_half