import requests
from typing import List, Dict


class SofaScoreClient:
    BASE_URL = "https://api.sofascore.com/api/v1"
    DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self, session: requests.Session | None = None, headers: Dict | None = None) -> None:
        self.session = session or requests.Session()
        self.headers = headers or self.DEFAULT_HEADERS

    def get_match_events(self, match_id: int) -> List[Dict]:
        """Fetch events for a given match using the unofficial SofaScore API."""
        url = f"{self.BASE_URL}/event/{match_id}/incidents"
        resp = self.session.get(url, headers=self.headers)
        resp.raise_for_status()
        data = resp.json()
        return data.get("incidents", [])

    def search_match(self, home_team: str, away_team: str) -> int | None:
        """Find a match ID by team names using the search endpoint."""
        query = f"{home_team} {away_team}"
        url = f"{self.BASE_URL}/search/all/{query}"
        resp = self.session.get(url, headers=self.headers)
        resp.raise_for_status()
        data = resp.json()
        for event in data.get("events", []):
            name = event.get("name", "").lower()
            if home_team.lower() in name and away_team.lower() in name:
                return event.get("id")
        return None


__all__ = ["SofaScoreClient"]
