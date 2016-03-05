
from flask import Blueprint, jsonify, request
from app.models import Affiliate
from app.scraper import webscraper, db_loader
from requests import ConnectionError

scraper_api = Blueprint('scraper_api', __name__)

import logging
my_logger = logging.getLogger("app.log")

@scraper_api.route('/scrape_affiliate', methods=['GET'])
def scrape():

    affiliate_id = request.args.get('affiliate_id')
    my_logger.info("Scraping Affiliate: %s" % affiliate_id)

    affiliate_record = Affiliate.query.filter_by(id=affiliate_id).one_or_none()

    if affiliate_record is not None:
        my_logger.info("Affiliate is all ready scraped.")
        return jsonify(**{'Message': 'Affiliate all ready scraped.' })

    try:
        affiliate_data = webscraper.affiliate_scraper(affiliate_id)
        my_logger.info("Finished Scraping Affiliate Data.")
    except ConnectionError as error:
        my_logger.error("Error: %s" % error)
        return jsonify(**{'Message': 'Affiliate Does Not Exists' })

    sql_affiliate_id = db_loader.load_affiliate_data(affiliate_data)
    athlete_data = webscraper.affiliate_athletes_scraper()
    athletes = db_loader.load_athlete_data(athlete_data, sql_affiliate_id)

    message = 'Scraped %s Athletes.' % len(athlete_data)
    return jsonify(**{'Message': message })