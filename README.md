# Instagram Profile Scraper API

A Python-based Instagram profile data extraction project built with **Scrapy, Playwright, and FastAPI**. It demonstrates browser automation, HTML parsing, authenticated session handling, and structured JSON extraction.

## Features

- Extracts selected Instagram profile information.
- Supports a username parameter for choosing the target profile.
- Uses Scrapy and Playwright to process dynamically rendered pages.
- Supports Playwright authentication state supplied by the user.
- Provides a FastAPI interface for requesting profile data.
- Exports structured JSON results.

## Technologies

- Python
- Scrapy
- Playwright
- scrapy-playwright
- FastAPI
- Uvicorn

## Project Structure

```text
instagram-profile-scraper-demo/
├── instagram/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── nike_profile.py
├── main.py
├── scraper.py
├── scrapy.cfg
├── requirements.txt
├── nike.json
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shariqmumtaz-commits/instagram-profile-scraper-demo.git
cd instagram-profile-scraper-demo
```

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Authentication

The spider expects a valid Playwright storage-state file named `state.json` in the repository's root directory, or JSON storage-state content supplied through the `INSTAGRAM_STATE` environment variable.

The storage state must be generated from an authorized Instagram session.

For security reasons, authentication files, passwords, cookies, and session tokens are not included in this repository.

## Running the Spider

Check whether Scrapy recognizes the spider:

```bash
scrapy list
```

Run the spider for an example username:

```bash
scrapy crawl nike_profile -a username=nike -O nike.json
```

A valid authorized authentication state must be configured before running the spider.

## Running the API

Start FastAPI:

```bash
uvicorn main:app --reload
```

Example endpoint:

```text
GET http://127.0.0.1:8000/scrape?username=nike
```

The API invokes the Scrapy spider and returns the collected data in JSON format.

## Example Output

An example of the extracted data structure:

```json
{
  "username": "nike",
  "full_name": "Nike",
  "bio": "Just Do It.",
  "posts": "1,626 posts",
  "followers": "297M followers",
  "following": "240 following"
}
```

These values are illustrative of the included `nike.json` sample and should not be interpreted as current Instagram statistics.

## Known Limitations

- The project requires valid, authorized Instagram authentication state.
- Instagram's HTML structure and interface can change, affecting extraction.
- Some profile fields may be unavailable or returned as null.
- The current parser depends partly on text extracted from the profile header.
- The scraper uses fixed browser waits, which may not accommodate all loading conditions.
- Instagram access restrictions, session expiry, or HTTP errors may prevent successful extraction.
- The API currently invokes Scrapy through a subprocess without an explicit execution timeout.
- This is a portfolio demonstration, not a guaranteed production-ready scraping service.

## Responsible Use

This project is intended for demonstrating web scraping and API engineering techniques. Use it only where you have appropriate authorization and comply with applicable platform rules, privacy requirements, and access restrictions.

## Author

Shariq Mumtaz

Python Developer — Web Scraping & Automation
