import requests

class APIClient:
    BASE_URL = "https://oracleapex.com/ords/espaciosdereserva/"
    HEADERS = {
        "User-Agent": "As_espacio_mobile/1.0",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    @classmethod
    def get(cls, endpoint, params=None):
        url = cls.BASE_URL + endpoint
        response = requests.get(url, headers=cls.HEADERS, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    @classmethod
    def post(cls, endpoint, payload: dict):
        url = cls.BASE_URL + endpoint
        response = requests.post(url, json=payload, headers=cls.HEADERS, timeout=15)
        response.raise_for_status()
        return response.json()

    @classmethod
    def put(cls, endpoint, payload: dict):
        url = cls.BASE_URL + endpoint
        response = requests.put(url, json=payload, headers=cls.HEADERS, timeout=15)
        response.raise_for_status()
        return response.json()

    @classmethod
    def delete(cls, endpoint):
        url = cls.BASE_URL + endpoint
        response = requests.delete(url, headers=cls.HEADERS, timeout=15)
        response.raise_for_status()
        return response.status_code
