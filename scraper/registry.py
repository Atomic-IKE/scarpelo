# scraper/registry.py
import os
import importlib
import re
from urllib.parse import urlparse

class ScraperRegistry:
    _registry = []

    @classmethod
    def register(cls, *urls):
        """Decorator to register a scraper with a list of exact URLs"""
        def decorator(scraper_cls):
            # Store the exact URLs (parsed into a normalized format)
            normalized_urls = [cls._normalize_url(url) for url in urls]
            cls._registry.append((normalized_urls, scraper_cls))
            return scraper_cls
        return decorator

    @classmethod
    def get_scraper(cls, url):
        """Find the appropriate scraper class based on the exact URL"""
        normalized_url = cls._normalize_url(url)
        for urls, scraper_cls in cls._registry:
            if normalized_url in urls:
                return scraper_cls
        raise ValueError(f"No scraper found for URL: {url}")

    @staticmethod
    def _normalize_url(url):
        """Normalize URL by removing trailing slashes and ensuring it's in a consistent format"""
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}"



    @classmethod
    def load_plugins(cls):
        """Dynamically load all scraper plugins from the 'plugins' folder"""
        plugins_path = os.path.join(os.path.dirname(__file__), 'plugins')
        for file in os.listdir(plugins_path):
            if file.endswith('.py') and file != '__init__.py':
                module_name = f'scraper.plugins.{file[:-3]}'
                importlib.import_module(module_name)

# Call this function at the start of your application to dynamically load scrapers
ScraperRegistry.load_plugins()
