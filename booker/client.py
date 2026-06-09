import requests
from typing import Optional, Dict, Any


class BookerClient:
    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or "https://restful-booker.herokuapp.com"
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def create_booking(self, payload: Dict[str, Any]) -> requests.Response:
        return self.session.post(self._url('/booking'), json=payload)

    def get_booking(self, booking_id: int) -> requests.Response:
        return self.session.get(self._url(f'/booking/{booking_id}'))

    def update_booking(self, booking_id: int, payload: Dict[str, Any], token: str) -> requests.Response:
        headers = {'Cookie': f'token={token}'}
        return self.session.put(self._url(f'/booking/{booking_id}'), json=payload, headers=headers)

    def partial_update_booking(self, booking_id: int, payload: Dict[str, Any], token: str) -> requests.Response:
        headers = {'Cookie': f'token={token}'}
        return self.session.patch(self._url(f'/booking/{booking_id}'), json=payload, headers=headers)

    def delete_booking(self, booking_id: int, token: str) -> requests.Response:
        headers = {'Cookie': f'token={token}'}
        return self.session.delete(self._url(f'/booking/{booking_id}'), headers=headers)

    def auth(self, username: str, password: str) -> requests.Response:
        return self.session.post(self._url('/auth'), json={'username': username, 'password': password})
