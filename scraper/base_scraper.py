# scraper/base_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.browser_options import get_chrome_options
from selenium.webdriver.common.by import By
import os


class BaseScraper:
    def __init__(self, screenshot=False):
        self.driver = self.create_driver()
        self.screenshot_enabled = screenshot

    def create_driver(self):
        chrome_options = Options()

        chrome_options = get_chrome_options()
        # Initialize the Chrome driver
        
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def load_page(self, url):
        self.driver.get(url)
        # If screenshot is enabled, capture the screenshot
        if self.screenshot_enabled:
            print("Taking screenshot...")
            self.take_screenshot(url)

    def take_screenshot(self, url):
        """Takes a screenshot and saves it to the 'screenshots' folder."""
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        
        # Create a valid filename from the URL
        filename = f"screenshots/{url.replace('https://', '').replace('http://', '').replace('/', '_')}.png"
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")

    def get_title(self):
        """Fetch the title of the current page"""
        return self.driver.title

    def close(self):
        self.driver.quit()
