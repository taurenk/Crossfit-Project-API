
from flask import Blueprint, jsonify, request
from app.scraper import webscraper, db_loader

scraper_api = Blueprint('scraper_api', __name__)


@scraper_api.route('/scrape_affiliate', methods=['GET'])
def scrape():
    affiliate_id = request.args.get('affiliate_id')
    print "SCRAPING AFFILIATE ID: %s" % affiliate_id

    athlete_data = webscraper.affiliate_athletes_scraper()
    db_loader.load_athlete_data(athlete_data)

    message = 'Scraped %s Athletes.' % len(athlete_data)
    return jsonify(**{'Success': message })