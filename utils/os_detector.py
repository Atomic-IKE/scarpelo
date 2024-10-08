# utils/os_detector.py
import platform

def detect_os():
    """Returns the name of the operating system."""
    return platform.system().lower()
