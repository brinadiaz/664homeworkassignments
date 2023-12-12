import requests
import json
import time

search_endpoint = "https://collectionapi.metmuseum.org/public/collection/v1/search"

search_params = {
    'q': 'van gogh',
    'isOnView': 'true',
    'hasImages': 'true'
}

search_response = requests.get(search_endpoint, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()

    object_ids = search_data.get('objectIDs', [])

    object_titles = []

    for object_id in object_ids:
        object_detail_url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}'

        object_detail_response = requests.get(object_detail_url)

        if object_detail_response.status_code == 200:
            object_detail_data = object_detail_response.json()

            title = object_detail_data.get('title', 'Title not available')
            object_titles.append(title)

            print(f"\nDetailed information for object ID {object_id}:")
            print(json.dumps(object_detail_data, indent=2))
        else:
            print(f"\nError retrieving detailed information for object ID {object_id}. Status code: {object_detail_response.status_code}")

        time.sleep(1)

    print("\nList of Object Titles:")
    print(json.dumps(object_titles, indent=2))

else:
    print(f"Error: {search_response.status_code}")
