# 🎧 Spotify Data Analytics Dashboard 🎵

This project showcases an end-to-end Spotify analytics solution — from **data extraction using Python**, **database management with MySQL**, to building an **interactive dashboard in Power BI**. It explores track-level insights such as popularity, audio features, and streaming trends by integrating the Spotify Web API.
![Dashboard Preview](![Untitled design](https://github.com/user-attachments/assets/52ed1c3c-44f5-40de-a6cb-784b1d72a27b)
---

## 🚀 What This Project Covers

### 1. 🐍 Python (ETL Layer)
- Utilizes the [Spotify Web API](https://developer.spotify.com/documentation/web-api/) through the `spotipy` library
- Fetches track metadata such as:
  - Track name
  - Artist
  - Duration
  - Popularity
  - Acousticness, Danceability, Valence, etc.
- Stores the cleaned data in:
  - A **CSV file** (`spotify_track_data.csv`)
  - A **MySQL database**

### 2. 🗃️ MySQL (Data Storage & Querying)
- Schema creation and table design to store Spotify track data
- SQL queries to:
  - Rank tracks by popularity or stream count
  - Calculate average metrics
  - Analyze trends across artists or dates

### 3. 📊 Power BI (Data Visualization)
An interactive Power BI dashboard built on top of the Spotify dataset with insights including:
- 💥 **Top streamed tracks**
- 🎯 **Danceability, Acousticness, Valence %**
- 📆 **Weekly and monthly track trends**
- 📈 **Streams over time**
- 🧠 **Target analysis visual** for danceability or mood
- 🎨 **Album art rendered dynamically using HTML Viewer**

---

## 🧰 Tech Stack

| Tool         | Purpose                                      |
|--------------|----------------------------------------------|
| Python       | Data extraction from Spotify API             |
| Spotipy      | Spotify Web API wrapper                      |
| Pandas       | Data manipulation and cleaning               |
| Matplotlib   | Initial data visualization                   |
| MySQL        | Structured storage and SQL analysis          |
| Power BI     | Dashboard development and reporting          |
| HTML Viewer  | For rendering album art in Power BI          |

---




