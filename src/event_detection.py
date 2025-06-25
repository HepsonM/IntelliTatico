from typing import List, Dict

from services.sofascscore import SofaScoreClient


def fetch_critical_events(match_id: int) -> List[Dict]:
    """Return a list of critical events for a match."""
    client = SofaScoreClient()
    events = client.get_match_events(match_id)
    critical_types = {"goal", "miss", "yellow-card", "red-card", "substitution"}
    return [e for e in events if e.get("incidentType") in critical_types]


__all__ = ["fetch_critical_events"]
