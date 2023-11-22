from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    api_key = os.getenv('6d1057d6d3c351b52cb25a836a489eff')  # Set your API key as an environment variable
    city = request.form.get('city')

    if not city:
        return 'Please provide a city.'

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # You can adjust units as needed
    }

    response = requests.get(url, params=params)
    data = response.json()

    return f'Temperature in {city}: {data["main"]["temp"]}°C'


if __name__ == '__main__':
    app.run(debug=True)
