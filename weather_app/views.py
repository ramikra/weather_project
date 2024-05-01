from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('weather')  # Redirect to the weather page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def weather(request):
    # Base API endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = '9200d9c689effaf05c9797fe24efb715'
    user_location = {
        'user1': {'lat': '59.857747', 'lon': '17.646817'},  # Uppsala
        'user2': {'lat': '57.708707', 'lon': '11.973271'}   # Göteborg
    }
    location = user_location.get(request.user.username)
    if location:
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(url, params=params)
        weather_data = response.json()
        data = response.json()

        # Extract the data
        weather_data = {
            'location': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return render(request, 'weather.html', {'weather': weather_data})
    else:
        return redirect('login')
