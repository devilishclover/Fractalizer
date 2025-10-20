"""
Video rendering and file management for fractal animations.
"""

import os
import sys
import glob
from pathlib import Path


class VideoRenderer:
    """Handles video compilation and cleanup of temporary files."""
    
    def __init__(self, fps=30, quality='high'):
        """
        Initialize video renderer.
        
        Args:
            fps (int): Frames per second for output video
            quality (str): Video quality ('low', 'medium', 'high', 'lossless')
        """
        self.fps = fps
        self.quality = quality
        self.quality_settings = {
            'low': {'crf': 28, 'preset': 'fast'},
            'medium': {'crf': 23, 'preset': 'medium'},
            'high': {'crf': 18, 'preset': 'slow'},
            'lossless': {'crf': 0, 'preset': 'veryslow'}
        }
        
    def compile_to_mp4(self, temp_files, output_path):
        """
        Convert sequence of images to MP4 video.
        
        Args:
            temp_files (list): List of temporary image file paths
            output_path (str): Output video file path
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not temp_files:
            print("No temporary files to compile", file=sys.stderr)
            return False
            
        # Ensure output directory exists
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Try different video creation methods in order of preference
        methods = [
            self._try_ffmpeg,
            self._try_opencv,
            self._try_imageio
        ]
        
        for method in methods:
            try:
                if method(temp_files, output_path):
                    print(f"Video successfully created: {output_path}", file=sys.stderr)
                    return True
            except Exception as e:
                print(f"Method {method.__name__} failed: {e}", file=sys.stderr)
                continue
                
        print("All video creation methods failed. Please install ffmpeg, opencv-python, or imageio.", 
              file=sys.stderr)
        return False
        
    def _try_ffmpeg(self, temp_files, output_path):
        """Try to create video using ffmpeg command line tool."""
        import subprocess
        
        # Check if ffmpeg is available
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
            
        # Create a temporary file list for ffmpeg
        temp_dir = Path(temp_files[0]).parent
        file_list_path = temp_dir / 'file_list.txt'
        
        with open(file_list_path, 'w') as f:
            for file_path in sorted(temp_files):
                # Use absolute path to avoid directory issues
                abs_path = Path(file_path).resolve()
                f.write(f"file '{abs_path}'\n")
                
        quality_opts = self.quality_settings[self.quality]
        
        # FFmpeg command
        cmd = [
            'ffmpeg', '-y',  # Overwrite output file
            '-f', 'concat',
            '-safe', '0',
            '-i', str(file_list_path),
            '-c:v', 'libx264',
            '-preset', quality_opts['preset'],
            '-crf', str(quality_opts['crf']),
            '-r', str(self.fps),
            '-pix_fmt', 'yuv420p',
            str(output_path)
        ]
        
        # Run ffmpeg
        result = subprocess.run(cmd, cwd=temp_dir, 
                              capture_output=True, text=True)
        
        # Clean up file list
        file_list_path.unlink(missing_ok=True)
        
        if result.returncode != 0:
            print(f"FFmpeg error: {result.stderr}", file=sys.stderr)
            return False
            
        return True
        
    def _try_opencv(self, temp_files, output_path):
        """Try to create video using OpenCV."""
        try:
            import cv2
            import numpy as np
            from PIL import Image
        except ImportError:
            return False
            
        if not temp_files:
            return False
            
        # Read first image to get dimensions
        first_image = Image.open(temp_files[0])
        width, height = first_image.size
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(str(output_path), fourcc, self.fps, (width, height))
        
        if not video_writer.isOpened():
            return False
            
        # Add each frame to video
        for file_path in sorted(temp_files):
            image = Image.open(file_path)
            
            # Convert PIL image to OpenCV format
            opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            video_writer.write(opencv_image)
            
        video_writer.release()
        return True
        
    def _try_imageio(self, temp_files, output_path):
        """Try to create video using imageio."""
        try:
            import imageio
        except ImportError:
            return False
            
        if not temp_files:
            return False
            
        # Read all images
        images = []
        for file_path in sorted(temp_files):
            images.append(imageio.imread(file_path))
            
        # Create video
        imageio.mimsave(str(output_path), images, fps=self.fps, quality=8)
        return True
        
    def cleanup_temp_files(self, temp_files):
        """
        Remove temporary image files.
        
        Args:
            temp_files (list): List of temporary file paths to remove
        """
        removed_count = 0
        failed_count = 0
        
        for file_path in temp_files:
            try:
                Path(file_path).unlink(missing_ok=True)
                removed_count += 1
            except Exception as e:
                print(f"Failed to remove {file_path}: {e}", file=sys.stderr)
                failed_count += 1
                
        print(f"Cleanup complete: {removed_count} files removed", file=sys.stderr)
        if failed_count > 0:
            print(f"Warning: {failed_count} files could not be removed", file=sys.stderr)
            
    def cleanup_temp_directory(self, temp_dir):
        """
        Clean up entire temporary directory.
        
        Args:
            temp_dir (str): Path to temporary directory
        """
        temp_path = Path(temp_dir)
        if not temp_path.exists():
            return
            
        # Remove all PNG files in temp directory
        png_files = list(temp_path.glob("*.png"))
        if png_files:
            self.cleanup_temp_files([str(f) for f in png_files])
            
        # Remove directory if empty
        try:
            temp_path.rmdir()
        except OSError:
            # Directory not empty, that's okay
            pass