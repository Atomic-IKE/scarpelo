# scraper/scraper_selector.py
from scraper.registry import ScraperRegistry

class ScraperSelector:
    @staticmethod
    def get_scraper(url):
        return ScraperRegistry.get_scraper(url)
