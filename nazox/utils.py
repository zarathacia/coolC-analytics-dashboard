import json

def from_Byte_toJson(data):
        data_t = data.content.decode('utf8').replace("'", '"')
        data = json.loads(data_t)
        return data

def diff(dif):
    if(dif==0):
        return ("No changes","mdi-minus","danger")
    if(dif>0):
        return ("Hotter From previous temp","mdi-menu-up","secondary")
    if(dif<0):
        return ("Cooler From previous temp","mdi-menu-down","info")

def weatherState(dif):
    if(dif=="Thunderstorm"):
        return "mdi-weather-lightning-rainy"
    if(dif=="Drizzle"):
        return "mdi-weather-pouring"
    if(dif=="Rain"):
        return " mdi-weather-rainy"
    if(dif=="Snow"):
        return "mdi-weather-snowy-heavy"
    if(dif=="Clouds"):
        return "mdi-weather-cloudy"
    return "mdi-weather-sunny"    

def predict(tmp):
    if (tmp>30):
        return 24
    elif(tmp>25): 
        return tmp-1
    elif(tmp>20):
        return tmp 
    else:
        return 22