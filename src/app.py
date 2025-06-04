#!/usr/bin/env python3
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Ensure the instance folder exists
if not os.path.exists(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance')):
    os.makedirs(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance'))

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
db_path = os.path.join(basedir, 'instance', 'weather.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Models ---
class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    sleep_hours = db.Column(db.Float)
    water_ml = db.Column(db.Integer)
    mood = db.Column(db.String(20))

    def __repr__(self):
        return f'<HealthRecord {self.id}: {self.sleep_hours}h sleep, {self.water_ml}ml water, {self.mood}>'

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float, nullable=False)

# --- Create tables once ---
with app.app_context():
    db.create_all()

# --- Routes ---

@app.route("/", methods=["GET"])
def index():
    return '''
        <form action="/submit" method="post">
            Sleep hours: <input name="sleep"><br>
            Water (ml): <input name="water"><br>
            Mood: <input name="mood"><br>
            <input type="submit" value="Submit!">
        </form>
    '''

@app.route("/submit", methods=["POST"])
def submit():
    sleep = request.form.get("sleep", 0)
    water = request.form.get("water", 0)
    mood = request.form.get("mood", "")
    record = HealthRecord(sleep_hours=sleep, water_ml=water, mood=mood)
    db.session.add(record)
    db.session.commit()
    return f"Submitted: {sleep} hours sleep, {water}ml water, mood: {mood}"

@app.route("/records")
def records():
    all_records = HealthRecord.query.order_by(HealthRecord.date.desc()).all()
    output = ""
    for rec in all_records:
        output += f"Date: {rec.date.strftime('%Y-%m-%d %H:%M')}, Sleep: {rec.sleep_hours}, Water: {rec.water_ml}, Mood: {rec.mood}<br>"
    return output

@app.route("/weather_records")
def weather_records():
    all_weather = Weather.query.order_by(Weather.datetime.desc()).all()
    output = ""
    for rec in all_weather:
        output += f"Time: {rec.datetime.strftime('%Y-%m-%d %H:%M')}, Temp: {rec.temperature}°C<br>"
    return output

@app.route('/average/<start_date>/<end_date>')
def average_temperature(start_date, end_date):
    records = Weather.query.filter(
        Weather.datetime >= start_date,
        Weather.datetime <= end_date
    ).all()

    if not records:
        return jsonify({"error": "No records found"}), 404

    avg_temp = sum(r.temperature for r in records) / len(records)

    return jsonify({
        "start_date": start_date,
        "end_date": end_date,
        "average_temperature": avg_temp
    })

def calc_health_score(sleep_hours, water_ml):
    """
    A simple health score calculation logic for unit testing.
    """
    score = 0
    try:
        sh = float(sleep_hours)
        w = float(water_ml)
    except:
        return 0
    if sh >= 8:
        score += 50
    elif sh >= 6:
        score += 30
    else:
        score += 10
    if w >= 2000:
        score += 50
    elif w >= 1000:
        score += 30
    else:
        score += 10
    return score

if __name__ == "__main__":
    app.run(debug=True)
