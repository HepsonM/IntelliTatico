from pathlib import Path
from typing import List, Dict


class VideoPipeline:
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_events(self, video_path: Path, events: List[Dict]) -> List[Path]:
        """Given a full match video and event list, return paths to clips."""
        # TODO: implement video cutting and analysis
        clips: List[Path] = []
        return clips


__all__ = ["VideoPipeline"]
