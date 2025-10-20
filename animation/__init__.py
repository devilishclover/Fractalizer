"""
Animation module for the Fractalizer.

This module provides classes and functionality for creating animated fractals
by interpolating between different parameter values and generating video output.
"""

from .animator import FractalAnimator
from .interpolator import LinearInterpolator, EaseInOutInterpolator
from .video_renderer import VideoRenderer
from .animation_config import AnimationConfig

__all__ = [
    'FractalAnimator',
    'LinearInterpolator', 
    'EaseInOutInterpolator',
    'VideoRenderer',
    'AnimationConfig'
]