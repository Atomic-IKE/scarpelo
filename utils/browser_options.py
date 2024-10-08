# utils/browser_options.py
from selenium.webdriver.chrome.options import Options
import utils.os_detector as os_detector

def get_chrome_options():
    """Returns the correct Chrome options based on the operating system."""
    chrome_options = Options()
    
    # Detect the operating system
    os_name = os_detector.detect_os()
    
    # Configure Chrome options based on the OS
    if os_name == 'linux':
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    else:
        chrome_options.add_argument('--start-maximized')

    return chrome_options
