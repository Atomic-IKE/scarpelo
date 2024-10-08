# Scarpelo

## Project Overview

**Scarpelo** is a web scraping tool designed for flexibility and ease of use. It leverages the power of Selenium to navigate and extract data from websites. With Scarpelo, users can scrape data from various sources and save screenshots of the pages they visit.

## Features

- **Multiple Source Options**: Scrape URLs from static configurations, command-line inputs, or API endpoints.
- **Screenshot Functionality**: Capture screenshots of web pages while scraping.
- **Plugin System**: Easily extend the functionality by adding new scraper plugins.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/scarpelo.git
   cd scarpelo
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Download and install ChromeDriver:

Ensure you have Google Chrome installed on your machine.

Download the ChromeDriver version that matches your Google Chrome version from ChromeDriver [Downloads](https://googlechromelabs.github.io/chrome-for-testing/#stable).

Make sure the ChromeDriver executable is in your system's PATH.

## Usage

To run the scraper, use the following command:

```bash
python3 run.py --source <source> --urls <url> [--api-url <api_url>] [--screenshot]
```

### Command-line Arguments

`--source`: Specify the source for URLs: `static`, `cli`, or `api`. Default is static.

`--urls`: List of URLs to scrape (required if source is cli).

`--api-url`: API endpoint to fetch URLs (required if source is api).

`--screenshot`: Enable screenshot functionality (optional).

## Example

To scrape a URL using the CLI and capture a screenshot, run:

```bash
python3 run.py --source cli --urls https://newsit.gr --screenshot
```

## How It Works

### Selenium and ChromeDriver

- Selenium is a powerful tool for controlling web browsers through programs. It provides a simple API to interact with web elements and navigate through pages.
- ChromeDriver is a standalone server that implements the WebDriver protocol for Chrome. It allows Selenium to communicate with the Chrome browser.

Scrapelo uses Selenium to launch a Chrome browser instance, navigate to the specified URLs, and extract data. Depending on the operating system, it can run Chrome in headless mode (on Linux) or in a regular window (on macOS and Windows).

## Contributing

Contributions to Scrapelo are welcome! Please fork the repository and submit a pull request. Make sure to follow the code style and include tests for any new features.

## License

This project is licensed under the MIT License.

Feel free to adjust any sections or content to better reflect your project's specifics!
