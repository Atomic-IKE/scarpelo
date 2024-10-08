# utils/url_provider.py
import argparse
import requests

class URLProvider:
    @staticmethod
    def get_static_urls():
        """Get URLs from a static configuration."""
        return ['https://newsit.gr']

    @staticmethod
    def get_cli_urls():
        """Get URLs from command-line arguments."""
        parser = argparse.ArgumentParser()
        parser.add_argument('urls', nargs='+', help='List of URLs to scrape')
        args = parser.parse_args()
        return args.urls

    @staticmethod
    def get_api_urls(api_url):
        """Fetch URLs from a 3rd-party API."""
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()['urls']
