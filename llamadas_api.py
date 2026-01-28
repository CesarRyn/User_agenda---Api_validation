import requests
def api_direccion(direccion):
    url = "https://nominatim.openstreetmap.org/search"
    parametros = {
        "q": direccion,
        "format": "json",
        "limit": 1,
        "addressdetails": 1
    }
    mis_headers = {
        "User-Agent": "mi-app"
    }
    response=requests.get(url, params=parametros, headers=mis_headers)
    data=response.json()
    if data == []:
        return data
    else:
        info=data[0]
        return info
