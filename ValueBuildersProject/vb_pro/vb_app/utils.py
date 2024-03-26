import requests
def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        data = response.json()  # assuming the API returns JSON data
        return data
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")
        return None
    
