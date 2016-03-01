
from flask import Blueprint
from app.scraper import webscraper

scraper_api = Blueprint('scraper_api', __name__)


@scraper_api.route('/scrape', methods=['GET'])
def scrape():
    print webscraper.scraper()
