import requests
from bs4 import BeautifulSoup

MOST_POPULAR_TVSHOWS_LINK = "https://www.imdb.com/chart/tvmeter/"
MOST_POPULAR_MOVIES_LINK = "https://www.imdb.com/chart/moviemeter/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def initialise_soup(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def get_top_50_links(soup):
    top_links = soup.select('.ipc-metadata-list-summary-item__tc a')
    all_links = []
    for link in top_links:
        all_links.append(link['href'].strip())
    return all_links[:50]


movies_soup = initialise_soup(MOST_POPULAR_MOVIES_LINK)
top_movies_links = get_top_50_links(movies_soup)

series_soup = initialise_soup(MOST_POPULAR_TVSHOWS_LINK)
top_series_links = get_top_50_links(series_soup)

print(top_movies_links)

print(top_series_links)


