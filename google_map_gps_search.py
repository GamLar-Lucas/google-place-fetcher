# Author: GamLar-Lucas

import requests  
import pandas as pd  
import time 

import key_const  # Module to import the Google API key

# Function to fetch nearby places with pagination handling
def fetch_places(location, radius, type_of_place):
    # URL for Google Places API Nearby Search endpoint
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    # Parameters for the API request
    params = {
        'location': location,    # Latitude,Longitude of the center
        'radius': radius,        # Radius in meters
        'type': type_of_place,   # Type of place to search (e.g., restaurant, cafe)
        'key': key_const.GOOGLE_API_KEY  # API key for authorization
    }

    # Initialize an empty list to collect data from all pages
    all_places = []

    while True:
        # Send a GET request to the Google Maps API with the specified parameters
        response = requests.get(url, params=params)
        places = response.json().get('results', [])  # Extract results from the API response
        
        # Loop through each place in the current page's results
        for place in places:
            # Extract relevant details about the place
            name = place.get('name')  # Name of the place
            rating = place.get('rating', 'N/A')  # Average rating (or 'N/A' if not available)
            user_ratings_total = place.get('user_ratings_total', 'N/A')  # Total user ratings
            address = place.get('vicinity', 'N/A')  # Address of the place
            place_id = place.get('place_id', 'N/A')  # Unique place identifier
            latitude = place['geometry']['location'].get('lat')  # Latitude of the place
            longitude = place['geometry']['location'].get('lng')  # Longitude of the place
            opening_hours = place.get('opening_hours', {}).get('open_now', 'N/A')  # Open status

            # Append the details to the list
            all_places.append([
                name, rating, user_ratings_total, address, place_id, latitude, longitude, opening_hours
            ])

        # Check for the next page token to determine if there are more results
        next_page_token = response.json().get('next_page_token')
        if next_page_token:
            # Update the parameters with the next page token and wait before the next request
            params['pagetoken'] = next_page_token
            print("Loading Next Page...")
            time.sleep(2)  # Delay to comply with API usage guidelines
        else:
            # No more pages; exit the loop
            break

    return all_places  # Return the collected data

# Function to save data to a CSV file
def save_to_csv(data, filename='places.csv'):
    # Create a DataFrame with the collected data
    df = pd.DataFrame(data, columns=[
        'Name', 'Rating', 'User Ratings Count', 'Address', 'Place ID', 'Latitude', 'Longitude', 'Currently Open'
    ])
    print(df) 
    df.to_csv(filename, index=False) 
    print(f"Data saved to {filename}")  

# Main execution block
if __name__ == "__main__":    
    # Prompt the user for GPS coordinates of the location
    location_GPS = input("Enter the GPS location (Lat,Lng) (e.g., '24.501214492234446,54.38865365016008'): ")
    while True:
        try:
            # Prompt the user for the search radius in meters
            radius = int(input("Enter the search radius in meters (e.g., 1000): "))
            if radius > 0:
                break
            else:
                print("Radius must be a positive number.")
        except ValueError:
            # Handle invalid input for radius
            print("Please enter a valid number.")

    # Prompt the user for the type of place to search
    type_of_place = input("Enter the type of place to search (e.g., 'restaurant', 'cafe', 'hotel'): ").strip()
    # Prompt the user for the output CSV file name or use the default name
    output_file = input("Enter the name of the output CSV file (default: 'places.csv'): ").strip() or "places.csv"

    print("\nFetching data, please wait...")
    place_data = fetch_places(location_GPS, radius, type_of_place)

    # Save the fetched data to the specified CSV file
    save_to_csv(place_data, output_file)