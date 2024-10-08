# run.py
from scraper.scaper_selector import ScraperSelector
from utils.url_provider import URLProvider
from utils.logger import logger
import argparse


def main():
    parser = argparse.ArgumentParser(description="Run the web scraper.")
    parser.add_argument('--source', choices=['static', 'cli', 'api'], default='static',
                        help="Specify the source for URLs: static, cli, or api.")
    parser.add_argument('--api-url', type=str, help="API endpoint to fetch URLs (required if source is 'api').")
    parser.add_argument('--urls', nargs='*', help="List of URLs to scrape (required if source is 'cli').")
    parser.add_argument('--screenshot', action='store_true', help="Enable screenshot functionality.")

    
    args = parser.parse_args()

    if args.source == 'static':
        urls = URLProvider.get_static_urls()
    elif args.source == 'cli':
        if not args.urls:
            raise ValueError("When using --source cli, you must provide --urls.")
        urls = args.urls
    elif args.source == 'api':
        if not args.api_url:
            raise ValueError("API URL is required when source is 'api'.")
        urls = URLProvider.get_api_urls(args.api_url)

    try:
        logger.info("Starting the scraping process...")
        
        for url in urls:
            logger.info(f"Processing URL: {url}")
            scraper_cls = ScraperSelector.get_scraper(url)
            scraper = scraper_cls(screenshot=args.screenshot)
            scraper.scrape(url)

        logger.info("Scraping completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
