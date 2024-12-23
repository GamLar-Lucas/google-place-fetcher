# Google Places Data Fetcher

A Python script that fetches information about nearby places using the Google Places API. This tool allows users to search for various types of places (restaurants, cafes, hotels, etc.) within a specified radius of a given GPS location.

## Features

- Search for places by type (restaurant, cafe, hotel, etc.)
- Customizable search radius
- Automatic pagination handling for comprehensive results
- Data collection includes:
  - Place name
  - Rating
  - Number of user ratings
  - Address
  - Place ID
  - GPS coordinates (latitude/longitude)
  - Current opening status

## Prerequisites

- Python 3.x
- Google Maps API key

## Required Python Packages

```
requests
pandas
```

Install the required packages using pip:

```bash
pip install requests pandas
```

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/GamLar-Lucas/google-place-fetcher.git
   cd google-place-fetcher
   ```

2. Create a `key_const.py` file in the project directory with your Google API key:
   ```python
   GOOGLE_API_KEY = "your-api-key-here"
   ```

## Usage

Run the script using Python:

```bash
python google_map_gps_search.py
```

The script will prompt you for:
1. GPS coordinates (latitude,longitude)
2. Search radius in meters
3. Type of place to search for
4. Output CSV filename (optional)

Example inputs:
```
Enter the GPS location (Lat,Lng): 24.501214492234446,54.38865365016008
Enter the search radius in meters: 1000
Enter the type of place to search: restaurant
Enter the name of the output CSV file: restaurants.csv
```

## Output

The script generates a CSV file containing the following information for each place:
- Name
- Rating
- User Ratings Count
- Address
- Place ID
- Latitude
- Longitude
- Currently Open status

## Important Notes

- The script includes a 2-second delay between paginated requests to comply with Google's API usage guidelines
- Make sure your Google API key has the necessary permissions and quota for Places API requests
- Keep your API key confidential and never commit it to version control

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
