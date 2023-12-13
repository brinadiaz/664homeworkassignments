import requests
from bs4 import BeautifulSoup
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# Function to scrape the Philips collection
def scrape_philips_collection():
    url = "https://www.phillipscollection.org/collection?on_view=1&has_image=1"  # Updated URL

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Adjust the following selectors based on the website structure
        artwork_elements = soup.select('.artwork-class')  # Replace with the actual class or selector

        # Create an array to store artist names
        artist_names = []

        for artwork in artwork_elements:
            # Adjust the following selectors based on the website structure
            artist_name = artwork.select_one('.artist-name-class').text.strip()  # Replace with the actual class or selector
            artist_names.append(artist_name)

        return artist_names

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Scrape the Philips collection
    artist_names = scrape_philips_collection()

    if artist_names:
        # Print the array
        print(artist_names)
    else:
        print("Error occurred during scraping.")

    # Add a small sleep to avoid overwhelming the server
    time.sleep(2)
