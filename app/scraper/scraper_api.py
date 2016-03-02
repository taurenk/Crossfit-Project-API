
from flask import Blueprint, jsonify
from app.scraper import webscraper

scraper_api = Blueprint('scraper_api', __name__)


@scraper_api.route('/scrape', methods=['GET'])
def scrape():
    return jsonify(**webscraper.affiliate_athleres_scraper())
