# Selenium-Web-Crawler
This Python script uses Selenium to crawl a publicly shared Google Site and extract text content from internal pages.

Requirements: #pip install selenium
Python 3.x
selenium
Chrome browser + ChromeDriver (must match your Chrome version)

How it works:
Starts at the base URL.
Parses the domain to identify internal links.
Visits each internal page only once.
Collects and prints visible text.

Disclaimer:
Designed for Google Sites layout; may need adjustment for other sites.
Intended for educational or personal use only.
