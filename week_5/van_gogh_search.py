import requests
import json
import time

# MET Museum API Endpoint
api_endpoint = "https://collectionapi.metmuseum.org/public/collection/v1/search"

# Parameters for the search (van gogh, on view, has images)
params = {
    'q': 'van gogh',
    'isOnView': 'true',
    'hasImages': 'true'
}

# Send an HTTP GET request to the API endpoint
response = requests.get(api_endpoint, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract object IDs from the response
    object_ids = data.get('objectIDs', [])

    # Print the result with indentation for better readability
    print("List of Object IDs:")
    print(json.dumps(object_ids, indent=2))

    # Now, you can loop through the object IDs and retrieve more detailed information if needed
    for object_id in object_ids:
        # Construct the URL for detailed object information
        object_detail_url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}'

        # Send an HTTP GET request to get detailed object information
        object_detail_response = requests.get(object_detail_url)

        # Check if the request was successful (status code 200)
        if object_detail_response.status_code == 200:
            object_detail_data = object_detail_response.json()
            # Print detailed information with indentation for better readability
            print(f"\nDetailed information for object ID {object_id}:")
            print(json.dumps(object_detail_data, indent=2))
        else:
            print(f"\nError retrieving detailed information for object ID {object_id}. Status code: {object_detail_response.status_code}")

        # Introduce a delay of 1 second between requests
        time.sleep(1)

else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")