from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bf29b34601023cbcf8e0a21b03f33daa').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "humidity": str(json_data['main']['humidity']),
            "pressure": str(json_data['main']['pressure'])
        }
    else:
        city = ''
        data = ''
    return render(request, "index.html", {'city': city, 'data': data})