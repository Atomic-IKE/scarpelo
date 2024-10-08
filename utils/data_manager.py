# utils/data_manager.py
import json

class DataManager:
    @staticmethod
    def save_data(data):
        """Save scraped data to a JSON file."""
        with open('scraped_data.json', 'a') as f:
            json.dump(data, f)
            f.write("\n")
