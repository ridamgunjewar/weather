from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'location': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = 'bbc9b2ec2ee2a6a02b42655e9808b1e7'  # Replace with your OpenWeatherMap API key
        location = request.form['location']
        weather = get_weather(api_key, location)
        if weather:
            return render_template('weather.html', weather=weather)
        else:
            return render_template('weather.html', error="Failed to fetch weather data. Please check your location or API key.")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
