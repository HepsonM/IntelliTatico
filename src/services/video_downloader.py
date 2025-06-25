from pathlib import Path
from typing import Optional

import requests


class VideoDownloader:
    """Simple utility to download a video file from a given URL."""

    def __init__(self, session: Optional[requests.Session] = None) -> None:
        self.session = session or requests.Session()

    def download(self, url: str, dest: Path) -> Path:
        resp = self.session.get(url, stream=True)
        resp.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return dest


__all__ = ["VideoDownloader"]
