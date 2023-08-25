import requests
from bs4 import BeautifulSoup
import pandas as pd

MOST_POPULAR_TVSHOWS_LINK = "https://www.imdb.com/chart/tvmeter/"
MOST_POPULAR_MOVIES_LINK = "https://www.imdb.com/chart/moviemeter/"

# Headers to mimic a browser request, helping bypass potential scraping restrictions.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def initialise_soup(url):
    """
    Initialize a BeautifulSoup object given a URL.
    
    Args:
    - url (str): The URL to fetch the content from.

    Returns:
    - BeautifulSoup object.
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def get_top_50_links(soup):
    """
    Extract the top 50 movie or series links from IMDb's popular charts.
    
    Args:
    - soup (BeautifulSoup): BeautifulSoup object containing the page content.

    Returns:
    - List of top 50 links.
    """
    top_links = soup.select('.ipc-metadata-list-summary-item__tc a')
    all_links = [link['href'].strip() for link in top_links]
    return all_links[:50]

def get_details(url):
    """
    Extract key details for a movie or series from IMDb.
    
    Args:
    - url (str): The URL of the movie or series page.

    Returns:
    - Dictionary containing the movie or series details.
    """
    soup = initialise_soup(url)
    
    title = soup.select('h1[data-testid="hero__pageTitle"] span')[0].text

    year_elements = soup.select('.sc-acac9414-0 ul li')
    year_elem = year_elements[1].find('a') if len(year_elements) > 1 else None
    year = year_elem.text if year_elem else None

    genres = [item.text for item in soup.select('.ipc-chip-list__scroller a span')]

    rating_elem = soup.find(class_="sc-bde20123-1")
    rating = rating_elem.text if rating_elem else None
    
    duration = soup.select('.sc-acac9414-0 ul li')[-1].text

    synopsis_elem = soup.find('span', {'data-testid': 'plot-xs_to_m'})
    synopsis = synopsis_elem.text if synopsis_elem else None

    details = {
        "Title": title,
        "Year": year,
        "Genres": genres,
        "Rating": rating,
        "Duration": duration,
        "Synopsis": synopsis,
    }

    return details


# Initialize BeautifulSoup objects for the movie and series pages
movies_soup = initialise_soup(MOST_POPULAR_MOVIES_LINK)
top_movies_links = get_top_50_links(movies_soup)

series_soup = initialise_soup(MOST_POPULAR_TVSHOWS_LINK)
top_series_links = get_top_50_links(series_soup)

# Fetch details for each movie and series link
movie_details = [get_details(f"https://www.imdb.com{link}") for link in top_movies_links]
series_details = [get_details(f"https://www.imdb.com{link}") for link in top_series_links]

# Save the details to CSV files using pandas
pd.DataFrame(movie_details).to_csv('top_movies.csv', index=False)
pd.DataFrame(series_details).to_csv('top_series.csv', index=False)
