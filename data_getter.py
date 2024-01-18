import requests


class DataGetter:
    def __init__(self):
        self.static_maps_address = "http://static-maps.yandex.ru/1.x/"
        self.geocoder_address = "http://geocode-maps.yandex.ru/1.x"
        self.geocoder_api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

    def get_map_image(self, lon, lat, delta):
        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        response = requests.get(self.static_maps_address, params=params)
        return response.content

