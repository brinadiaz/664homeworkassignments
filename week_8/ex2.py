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

        # Create a list to store dictionaries for each artwork
        artworks_info = []

        for artwork in artwork_elements:
            # Adjust the following selectors based on the website structure
            artist_name = artwork.select_one('.artist-name-class').text.strip()  # Replace with the actual class or selector
            material = artwork.select_one('.material-class').text.strip()  # Replace with the actual class or selector
            dimensions = artwork.select_one('.dimensions-class').text.strip()  # Replace with the actual class or selector

            # Create a dictionary for each artwork
            artwork_info = {'artist': artist_name, 'material': material, 'dimensions': dimensions}
            
            # Append the dictionary to the list
            artworks_info.append(artwork_info)

        return artworks_info

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Scrape the Philips collection
    artworks_info = scrape_philips_collection()

    if artworks_info:
        # Print the list of dictionaries
        for artwork_info in artworks_info:
            print(artwork_info)
    else:
        print("Error occurred during scraping.")

    # Add a small sleep to avoid overwhelming the server
    time.sleep(2)
