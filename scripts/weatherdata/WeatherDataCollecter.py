import requests
import json

def updateURL():
    '''
    File DATA.txt containing:
        1 - API key
        2 - location
    ''' 
    DATA = open("DATA.txt")

    API_KEY = DATA.readline()
    PLACE = DATA.readline()
    NUMBER = '1'
    FORMAT = 'json'
    url = f"https://api.worldweatheronline.com/premium/v1/weather.ashx?key={API_KEY}&q={PLACE}&num_of_days={NUMBER}&format={FORMAT}"

    DATA.close()
    return url

def getweatherdata(url):
    response = requests.get(url)
    if response.status_code == 200: #Check API running
        currentdata = json.dumps(response.json(),indent=2)
        data = json.loads(currentdata)
        return data
    else:
        raise Exception("API error :",response.status_code)

URL = updateURL()

#Example request
#weatherdata = getweatherdata(URL)
#print(f'Temperature {weatherdata["data"]["current_condition"][0]["temp_C"]}°C')