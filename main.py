import os
import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
TMDB_API_KEY = os.getenv("TMDB_API_KEY", "YOUR_TMDB_API_KEY_HERE")
TMDB_BASE_URL = "https://api.themoviedb.org/3"
HORROR_GENRE_ID = "27"

# Manifest Definition
MANIFEST = {
    "id": "org.stremio.horrorarchive",
    "version": "1.0.0",
    "name": "The Horror Archive",
    "description": "A dedicated catalog for horror movies only.",
    "types": ["movie"],
    "catalogs": [
        {
            "type": "movie",
            "id": "horror_trending",
            "name": "Trending Horror",
            "extra": [{"name": "genre", "isRequired": False}]
        },
        {
            "type": "movie",
            "id": "horror_top_rated",
            "name": "Top Rated Horror",
            "extra": [{"name": "genre", "isRequired": False}]
        }
    ],
    "resources": ["catalog", "meta"],
    "idPrefixes": ["tmdb"]
}

def format_meta(tmdb_item):
    """Converts TMDB data format to Stremio Meta format."""
    return {
        "id": f"tmdb:{tmdb_item.get('id')}",
        "type": "movie",
        "name": tmdb_item.get("title"),
        "poster": f"https://image.tmdb.org/t/p/w500{tmdb_item.get('poster_path')}" if tmdb_item.get('poster_path') else None,
        "description": tmdb_item.get("overview"),
        "releaseInfo": tmdb_item.get("release_date", "")[:4],
        "imdbRating": str(tmdb_item.get("vote_average"))
    }

def fetch_horror_movies(sort_by="popularity.desc"):
    """Fetches horror movies from TMDB API."""
    try:
        url = f"{TMDB_BASE_URL}/discover/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "with_genres": HORROR_GENRE_ID,
            "sort_by": sort_by,
            "language": "en-US",
            "page": 1
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [format_meta(item) for item in data.get("results", [])]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/manifest.json')
def addon_manifest():
    return jsonify(MANIFEST)

@app.route('/catalog/movie/<catalog_id>.json')
def addon_catalog(catalog_id):
    metas = []
    
    if catalog_id == "horror_trending":
        metas = fetch_horror_movies(sort_by="popularity.desc")
    elif catalog_id == "horror_top_rated":
        metas = fetch_horror_movies(sort_by="vote_average.desc")
    else:
        abort(404)

    return jsonify({"metas": metas})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7000))
    app.run(host='0.0.0.0', port=port)
