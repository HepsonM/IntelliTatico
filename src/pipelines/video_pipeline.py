from pathlib import Path
from typing import List, Dict

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class VideoPipeline:
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_events(self, video_path: Path, events: List[Dict]) -> List[Path]:
        """Given a full match video and event list, return paths to clips."""
        clips: List[Path] = []
        for idx, event in enumerate(events, start=1):
            minute = event.get("time", {}).get("minute", 0)
            start = max(minute * 60 - 10, 0)
            end = start + 20
            out_path = self.output_dir / f"clip_{idx}.mp4"
            ffmpeg_extract_subclip(str(video_path), start, end, targetname=str(out_path))
            clips.append(out_path)
        return clips


__all__ = ["VideoPipeline"]
