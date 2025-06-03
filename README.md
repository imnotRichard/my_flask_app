# **Health Tracker & Weather Data Collector**

This project demonstrates how to fetch data from an external REST API and store it in a database, as required by the assignment. It is a simple Flask-based web application for health habit tracking, enhanced with a scheduled weather data collection feature.

## Features

· Submit and store daily health data (sleep hours, water intake, mood)

· Fetch the latest weather temperature from an external API and store it in a database

· View all health records and weather records from your browser

## Project Structure

- src/
  - app.py: Main Flask application (health records, database models, web routes)
- collect_weather.py: Script to fetch weather data from API and save to DB
- requirements.txt: Python dependencies
- Procfile: For Heroku deployment
- README.md: Project instructions
- .gitignore: Excludes venv, instance, and SQLite files from git

## Setup Instructions

### 1. Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. (Optional) Make sure the instance folder exists for database files:

```bash
mkdir -p instance
```


## Running the Application

### 1. Start the Flask server:

```bash
flask --app src/app.py run
```
Visit http://127.0.0.1:5000/ to use the web app.

### 2. Submit Health Records:

· Enter your daily sleep hours, water intake, and mood on the homepage.

· All records are saved to the database.

· View all records at: http://127.0.0.1:5000/records

### 3. Collect Weather Data:

· Run the script to fetch current temperature data and store it in the database:

```bash
python collect_weather.py
```
· View all weather records at: http://127.0.0.1:5000/weather_records


## Notes

The SQLite database files are created in the `instance/` directory.

## API Source

Weather data is fetched from [Open-Meteo API](https://open-meteo.com).