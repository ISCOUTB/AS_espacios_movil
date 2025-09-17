import requests

class APIClient:
    BASE_URL = "https://oracleapex.com/ords/espaciosdereserva/"
    HEADERS = {
        "User-Agent": "As_espacio_mobile/1.0",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # sesión persistente
    session = requests.Session()
    session.headers.update(HEADERS)

    @classmethod
    def ensure_cookies(cls):
        if not cls.session.cookies:
            resp = cls.session.get(cls.BASE_URL + "student_table/")
            resp.raise_for_status()

    @classmethod
    def get(cls, endpoint, params=None):
        cls.ensure_cookies()
        url = cls.BASE_URL + endpoint
        response = cls.session.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    @classmethod
    def post(cls, endpoint, payload: dict):
        cls.ensure_cookies()
        url = cls.BASE_URL + endpoint
        response = cls.session.post(url, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()

    @classmethod
    def put(cls, endpoint, payload: dict):
        cls.ensure_cookies()
        url = cls.BASE_URL + endpoint
        response = cls.session.put(url, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()

    @classmethod
    def delete(cls, endpoint):
        cls.ensure_cookies()
        url = cls.BASE_URL + endpoint
        response = cls.session.delete(url, timeout=15)
        if response.status_code == 204:
            return {"success": "Usuario eliminado correctamente"}
        elif response.status_code == 404:
            return {"error": "Usuario no encontrado"}
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
