# Crossfit-Project-API

REST API for Affiliate and Athlete data taken from games.crossfit.com. 

Goal 1: Make a dynamic web app that will allow a user to add their affiliate if it does not all ready exist in our database [would trigger scraper] and view stats + rankings of their athletes

Goal 2: Load the entire crossfit games athlete database into our DB. Make a dashboard of some stats we can derive from that data set. 

### Running:
pip install -r requirements.txt
python run.py


### Endpoints Needed:

api/affiliates
Does: Nothing for now
api/affiliates/<name> [or id?]
Does: Grab affiliate data for given affiliate
Response: 
{result: {‘id’: 123, ‘name’: ‘x’, ‘location’: ‘New York’}}
api/affiliates/<name>/athletes
Does: Grab all athletes for an affiliate.
Response: 
{results: {[
{‘id: 456, name: tauren, uri: xxx, openRank: 1},...
]} }

api/athletes
Does: Nothing for now
api/athletes/<name> [or id?]
Does: Give data + stats for given athlete
Response: {result: {}}

api/scrape_affiliate/<crossfit_affiliate_id>
Does: scapes affiliate + athlete data for give affiliate


### Schema
I hacked the schema a bit and put all scores embedded inside the athletes table.

