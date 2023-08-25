# IMDb Scraper

This script allows you to scrape IMDb's most popular movies and TV shows. It fetches details such as the title, release year, genres, rating, duration, and synopsis.

## Installation

1. Clone the repository:
```
git clone https://github.com/MariosAvraam/imdb-scraper.git
```

2. Navigate to the project directory:
```
cd imdb-scraper
```

3. (Optional) Set Up a Virtual Environment:
```
python -m venv venv
source venv/bin/activate #On Windows use venv\Scripts\activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

Run the script with Python:
```
python main.py
```


After running the script, you'll find two CSV files in your directory:

`top_movies.csv`: Contains details of the top 50 most popular movies.
`top_series.csv`: Contains details of the top 50 most popular TV shows.

## Data Columns:

The CSV files have the following columns:

`Title`: The name of the movie or series.
`Year`: The release year.
`Genres`: The genres associated with the movie or series.
`Rating`: The IMDb rating of the movie or series.
`Duration`: The duration of the movie or series.
`Synopsis`: A brief description or plot summary of the movie or series.

## Disclaimer
This code is intended for educational purposes only. Before using it for web scraping, make sure to review IMDb's terms of service and obtain the necessary permissions. Web scraping without permission can have legal implications.

## Contribution
If you'd like to contribute to this repository, please fork the repo and submit a pull request.

## License
This project is licensed under the MIT License.

## Notes:

Remember to always be respectful of the website's terms of service when using web scraping scripts. Websites can change their structure, so you might need to adjust the script in the future.

### Author:

Marios Avraam