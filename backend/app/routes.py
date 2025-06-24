import requests
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

load_dotenv()
UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY')

<<<<<<< HEAD
DATA_PATH = '../data/countries.json'
=======
DATA_PATH = 'backend/data/countries.json'
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)

# Load country data from JSON file
def load_countries():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
<<<<<<< HEAD
    

 #global variable countries   
=======

# Global variable countries   
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
countries = load_countries()

# Save country data to JSON file
def save_countries(data):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def fetch_image(country_name):
<<<<<<< HEAD
    # if no access key do nothing
=======
    # If no access key, do nothing
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
    if not UNSPLASH_ACCESS_KEY:
        return {"image_url": ""}
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": country_name,
        "per_page": 3,
        "client_id": UNSPLASH_ACCESS_KEY
    }
<<<<<<< HEAD
    # make get request
=======
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
    res = requests.get(url, params=params)
    if res.status_code == 200:
        results = res.json().get('results')
        if results and len(results) > 1:
<<<<<<< HEAD
            # get first picture
            image_url = results[2]['urls']['small']
            return {
                "image_url": image_url,
            }
    return {"image_url": ""}


=======
            image_url = results[2]['urls']['small']
            return {"image_url": image_url}
    return {"image_url": ""}

>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
@app.route('/')
@app.route("/home")
def home():
    sort_method = request.args.get('sort', default='popular')
    filter_type = request.args.get('type', default='all')

<<<<<<< HEAD
    countries = load_countries()

=======
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
    # Filter by type
    if filter_type.lower() in ['country', 'city']:
        filtered = [c for c in countries if c.get('type', 'country').lower() == filter_type.lower()]
    else:
        filtered = countries[:]

<<<<<<< HEAD
    # Sort by requested method
=======
    # Sort
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
    if sort_method == 'az':
        filtered.sort(key=lambda x: x.get('name', '').lower())
    elif sort_method == 'za':
        filtered.sort(key=lambda x: x.get('name', '').lower(), reverse=True)
    elif sort_method == 'popular':
        filtered.sort(key=lambda x: x.get('times_visited', 0), reverse=True)

<<<<<<< HEAD
    #fetch image for each country
=======
    # Fetch images
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
    for country in filtered:
        primary_name = country.get('name')
        unsplash_data = fetch_image(primary_name)
        country['image_url'] = unsplash_data['image_url']
    return jsonify(filtered)

<<<<<<< HEAD


@app.route('/country/<identifier>')
def country_page(identifier):
    found = False

    for country in countries:
        country["times_visited"] = country.get("times_visited", 0) + 1
        save_countries(countries)
        found = True
        # fetch Unsplash image
        primary_name = country.get('name')
        unsplash_data = fetch_image(primary_name)
        country['image_url'] = unsplash_data['image_url']
        return jsonify(country)

    if not found:
        return jsonify({"error": "Country not found"}), 404

=======
@app.route('/country/<country_code>')
def country_page(country_code):
    countries = load_countries()
    for country in countries:
        if country["code"].lower() == country_code.lower():
            country["times_visited"] = country.get("times_visited", 0) + 1
            save_countries(countries)
            return render_template('country.html', country=country)
    return "Country not found", 404
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)

@app.route('/map')
def map_page():
    GEOJSON_URL = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
    response = requests.get(GEOJSON_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return jsonify({"error": "Failed to fetch GeoJSON"}), 500

<<<<<<< HEAD

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
    
=======
# ✅ NEW API ROUTE for React CountryPage
@app.route('/api/country/<country_code>')
def api_get_country(country_code):
    countries = load_countries()
    for country in countries:
        if country["code"].lower() == country_code.lower():
            return jsonify(country)
    return jsonify({"error": "Country not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
