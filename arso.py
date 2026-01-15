import requests
url="https://vreme.arso.gov.si/api/1.0/location/?lang=sl&location=Kranj"
klic=requests.get(url).json()
print(klic["forecast3h"]["features"][0]["properties"]["days"][0]["timeline"][0]["t"])
