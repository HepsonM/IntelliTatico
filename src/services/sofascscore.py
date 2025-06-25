import requests
from typing import List, Dict


class SofaScoreClient:
    BASE_URL = "https://api.sofascore.com/api/v1"

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def get_match_events(self, match_id: int) -> List[Dict]:
        """Fetch events for a given match using the unofficial SofaScore API."""
        url = f"{self.BASE_URL}/event/{match_id}/incidents"
        resp = self.session.get(url)
        resp.raise_for_status()
        data = resp.json()
        return data.get("incidents", [])


__all__ = ["SofaScoreClient"]
