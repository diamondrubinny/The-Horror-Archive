# The Horror Archive - Stremio Addon

A dedicated Stremio catalog addon that filters and displays only horror movies using the TMDB API.

## Features
* **Curated Content:** Filters strictly by Genre ID 27 (Horror).
* **Dynamic Catalogs:** Supports "Trending Horror" and "Top Rated Horror".
* **Fast & Lightweight:** Built with Flask and deployed easily on serverless platforms.

## Setup Instructions

1.  **Get a TMDB API Key:**
    * Register at [The Movie Database](https://www.themoviedb.org/).
    * Go to Settings > API to generate a key.

2.  **Local Installation:**
    ```bash
    pip install -r requirements.txt
    export TMDB_API_KEY="your_key_here"
    python main.py
    ```

3.  **Deployment:**
    * This project is configured for Vercel deployment.
    * Install Vercel CLI or connect your GitHub repo to Vercel.
    * Add `TMDB_API_KEY` as an environment variable in Vercel settings.

4.  **Add to Stremio:**
    * Once deployed, paste your URL + `/manifest.json` into the Stremio search bar.
    * Example: `https://your-project.vercel.app/manifest.json`

## License
MIT License

