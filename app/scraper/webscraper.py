
from collections import defaultdict
from bs4 import BeautifulSoup
import requests


def affiliate_athletes_scraper(affiliate_id=3451):
    team_page = requests.get("http://games.crossfit.com/affiliate/%s" % affiliate_id)
    athletes = parse_athlete_data(team_page.content)
    for athlete_name, data in athletes.iteritems():
        stats = scrape_athlete_data(data['profile_url'])
        athletes[athlete_name].update(stats)
        print athlete_name

    print 'Loaded data for %s Athletes.' % len(athletes)
    return athletes


def affiliate_scraper(affiliate_id=3451):

    affiliate_data = {}

    team_page = requests.get("http://games.crossfit.com/affiliate/%s" % affiliate_id)
    soup = BeautifulSoup(team_page.content, "html.parser")

    profile_html =  soup.find(class_="profile-details")

    affiliate_data['affiliate_id'] = affiliate_id
    affiliate_data['logo_url'] = profile_html.find('img')['src']

    profile_details = profile_html.find_all("dd")

    affiliate_data['state'] = profile_details[3].text
    affiliate_data['country'] = profile_details[5].text

    return affiliate_data


def parse_athlete_data(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    roster_block = soup.find(id="block-search-athlete-affiliate-team-blocks-affiliate-athletes")
    roster_map = defaultdict(dict)

    for item in roster_block.find_all('li'):
        athlete_name = item.span.text
        athlete_data = {'profile_url': item.a['href'], 'image_url': item.img['src']}
        roster_map[athlete_name] = athlete_data

    return roster_map


def scrape_athlete_data(profile_url):

    athlete_page = requests.get("http://games.crossfit.com" + profile_url)
    soup = BeautifulSoup(athlete_page.content, "html.parser")
    athlete_data = {}

    stats = soup.find_all('dd')
    athlete_data['gender'] = stats[3].text
    athlete_data['age'] = stats[4].text
    athlete_data['height'] = stats[5].text
    athlete_data['weight'] = stats[6].text

    # Get Lifts
    for row in soup.find_all("tr"):
        if row.th is None:
            stats = row.find_all('td')
            stat = stats[0].text
            metric = stats[1].text
            if metric == '--':
                metric = None
            athlete_data[stat] = metric

    # Get Open Workout Scores - Athlete scoreboard is in Iframe:
    iframexx = soup.find_all('iframe')

    response = requests.get(iframexx[0].attrs['src'])
    iframe_soup = BeautifulSoup(response.content, "lxml")
    data = iframe_soup.find(class_="highlight")

    for index, score_html in enumerate(data.find_all('span', attrs={'data-scoreid' : True})):
        html = str(score_html)
        if "(" in html:
            key = "week_%s_score" % (index+1)
            athlete_data[key] = html[html.index("(")+1: html.index(")")]

    return athlete_data



if __name__ == '__main__':
    affiliate_scraper()