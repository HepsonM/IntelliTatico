from pathlib import Path
from typing import List, Dict

from moviepy.editor import VideoFileClip


class VideoPipeline:
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_events(self, video_path: Path, events: List[Dict]) -> List[Path]:
        """Given a full match video and event list, return paths to clips."""
        clips: List[Path] = []

        video = VideoFileClip(str(video_path))
        for idx, event in enumerate(events):
            minute = event.get("time", {}).get("minute", 0)
            second = event.get("time", {}).get("second", 0)
            event_time = minute * 60 + second

            start = max(0, event_time - 5)
            end = min(video.duration, event_time + 5)

            clip = video.subclip(start, end)
            out_name = f"clip_{idx}_{event.get('incidentType', 'event')}.mp4"
            out_path = self.output_dir / out_name
            clip.write_videofile(str(out_path), codec="libx264", audio=False, verbose=False, logger=None)
            clips.append(out_path)

        video.close()
        return clips


__all__ = ["VideoPipeline"]
