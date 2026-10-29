# 🎬 The Horror Archive — Stremio Addon

![License](https://img.shields.io/github/license/diamondrubinny/The-Horror-Archive?style=flat-square) ![Python](https://img.shields.io/badge/Python-Flask-3776AB?style=flat-square&logo=python&logoColor=white) ![Stremio](https://img.shields.io/badge/Stremio-addon-8A5AAB?style=flat-square)

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
    git clone https://github.com/diamondrubinny/The-Horror-Archive.git
    cd The-Horror-Archive
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
Distributed under the MIT License. See [LICENSE](LICENSE).

> This product uses the TMDB API but is not endorsed or certified by TMDB.

## 💼 Commercial license & rights acquisition

The Horror Archive is free and open source under the MIT License. If you are interested in a **commercial agreement** or custom licensing terms, **white-label / exclusive rights**, or **acquiring full rights to the code**, send your proposal to **[d@rubinny.net](mailto:d@rubinny.net)**.

Please include: who you are (company / contact), how you intend to use the code, and your offer.

> 🇮🇱 מעוניינים ברישיון מסחרי, בזכויות בלעדיות או ברכישת הזכויות בקוד? שלחו הצעה ל-**[d@rubinny.net](mailto:d@rubinny.net)** — כולל פרטי קשר, אופן השימוש המתוכנן וההצעה שלכם.

---

<sub>Created by **Diamond Rubinny** · © 2025–2026 Diamond Rubinny · [rubinny.co.il](https://rubinny.co.il)</sub>
