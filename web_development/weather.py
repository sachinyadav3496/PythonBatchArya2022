import requests 

def get_lat_lon(city_name):
    """
        will return a dictionary having latitude and longitude info
    """
    api_key = "390cfe9366e31568d802a3982999caab"
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"
    resp = requests.get(geo_url)
    if resp.status_code == 200:
        data = resp.json()
        if len(data) >= 1 and len(data[0]) >= 3:
            answer = {}
            answer["country"] = data[0]['country']
            answer["state"] = data[0]['state']
            if 'local_names' in data[0].keys():
                answer["name"] = data[0]['local_names']['hi']
            else:
                answer["name"] = data[0]['name']
            answer["lat"] = data[0]['lat']
            answer["lon"] = data[0]['lon']
            return answer
        else:
            print("Could not Get Data")
    else:
        print(f"Invalid Request! {resp.status_code}, {resp.reason}")
    return False

def get_temp(city_name):
    """
        will return temprature dictionary of city_name
    """
    info = get_lat_lon(city_name)
    api_key = "390cfe9366e31568d802a3982999caab"
    url = "https://api.openweathermap.org/data/2.5/weather"    
    if info:
        query_parameters = {
            "lat": info['lat'],
            "lon": info['lon'],
            "appid": api_key,
            "units": "metric"
        }
        resp = requests.get(url, params=query_parameters)
        if resp.status_code == 200:
            data = resp.json()
            if len(data) >= 3:
                info["desc"] = data["weather"][0]["description"]
                info["icon"] = data["weather"][0]["icon"]
                info["icon_url"] = f"https://openweathermap.org/img/wn/{info['icon']}@4x.png"
                info["temp"] = data["main"]["temp"]
                info["humidity"] = data["main"]['humidity']
                return info
            else:
                print("no weather information available")
        else:
            print(f"Could not fetch temprature! {resp.status_code} {resp.reason}")
    else:
        print("!Could Not get Lat and Lon, Please check location properly!")
    return False

if __name__ == "__main__":
    city = input("Enter city name: ")
    ans = get_temp(city)
    if ans:
        for key, value in ans.items():
            if 'icon' in key:
                continue
            print(f"{key:>30} = {value}")
    else:
        print("no data available")
