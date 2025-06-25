import requests
from typing import List, Dict


class SofaScoreClient:
    BASE_URL = "https://api.sofascore.com/api/v1"
    DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def get_match_events(self, match_id: int) -> List[Dict]:
        """Fetch events for a given match using the unofficial SofaScore API."""
        url = f"{self.BASE_URL}/event/{match_id}/incidents"
        resp = self.session.get(url, headers=self.DEFAULT_HEADERS)
        resp.raise_for_status()
        data = resp.json()
        return data.get("incidents", [])

    def search_match(self, home_team: str, away_team: str) -> List[Dict]:
        """Search for a match using the unofficial SofaScore API."""
        query = f"{home_team} {away_team}"
        encoded = requests.utils.quote(query)
        url = f"{self.BASE_URL}/search/all/{encoded}"
        resp = self.session.get(url, headers=self.DEFAULT_HEADERS)
        resp.raise_for_status()
        data = resp.json()
        events = data.get("events", [])
        filtered: List[Dict] = []
        for event in events:
            home = event.get("homeTeam", {}).get("name", "").lower()
            away = event.get("awayTeam", {}).get("name", "").lower()
            if home_team.lower() in home and away_team.lower() in away:
                filtered.append(event)
        return filtered


__all__ = ["SofaScoreClient"]
