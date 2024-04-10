import requests
from bs4 import BeautifulSoup
import csv

def scrape_top_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        movie_entries = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')[:20]
        data = [['Title', 'Year', 'Rating']]
        for entry in movie_entries:
            title = entry.find('h3').text
            year = entry.find('span', class_='cli-title-metadata-item').text
            rating = entry.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").get('aria-label').split(":")[1].strip()
            data.append([title, year, rating])
        return data
    else:
        print("Failed to fetch data from IMDb.")

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def average_rating(data):
    ratings = [float(row[2]) for row in data[1:]]  # Exclude header row
    return sum(ratings) / len(ratings)

url = 'https://www.imdb.com/chart/top/'

# Scrape top movies data
top_movies_data = scrape_top_movies(url)

# Write data to CSV file
output_file = 'top_movies.csv'
write_to_csv(top_movies_data, output_file)

# Calculate average rating
avg_rating = average_rating(top_movies_data)

print(f"Average rating of the top-rated movies: {avg_rating:.2f}")
