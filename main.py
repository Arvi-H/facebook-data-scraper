from getpass import getpass, getuser

# This file shows an example of how the system can be used.
# I think this should provide lots of flexibility for 
# different studies.

# Import the scraper and the scraper services required
# for the given study.
from scraper import Scraper
from frreqscrapeservice import FrReqScrapeService
from profscrapeservice import ProfScrapeService
from sheetsbackend import SheetsBackend

# Initialize the scraper with the credentials for the
# study participant (one-time passwords only!!!)
# Here, we read the credentials from env vars so that creds
# aren't being pushed to the public repo

scraper = Scraper(input('Username/Phone: '), getpass())

# Set the backend with the name of the keys file and spreadsheet ID
scraper.attach_backend(SheetsBackend('keys.json', '1oFPY4kaiqCih2FULkxqkjy8XbO5Vbya3HQku4w8Ys1g'))

# Attach the scrape services you'll be using.
scraper.attach_scraper(FrReqScrapeService())
scraper.attach_scraper(ProfScrapeService())

# Call scrape to gather all data
scraper.scrape()