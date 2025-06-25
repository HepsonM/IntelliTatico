from typing import List, Dict

from services.sofascscore import SofaScoreClient


def fetch_critical_events(match_id: int) -> List[Dict]:
    """Return a list of critical events for a match."""
    client = SofaScoreClient()
    events = client.get_match_events(match_id)
    critical_types = {"goal", "miss", "yellow-card", "red-card", "substitution"}
    return [e for e in events if e.get("incidentType") in critical_types]


def search_match_id(home_team: str, away_team: str) -> int | None:
    """Return the match id if found on SofaScore."""
    client = SofaScoreClient()
    matches = client.search_match(home_team, away_team)
    if not matches:
        return None
    return matches[0].get("id")


__all__ = ["fetch_critical_events", "search_match_id"]
