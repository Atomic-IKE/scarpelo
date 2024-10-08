# scraper/plugins/newsit_scraper.py
from scraper.base_scraper import BaseScraper
from scraper.registry import ScraperRegistry
from utils.data_manager import DataManager

# Register multiple patterns for the same site
@ScraperRegistry.register('https://newsit.gr')
class NewsitScraper(BaseScraper):
    def scrape(self, url):
        self.load_page(url)
        # Logging the url title
        title = self.driver.title
        print(f"Title: {title}")
        self.close()
        
        # # Save the data
        # DataManager.save_data({'url': url, 'data': text})
        # self.close()
