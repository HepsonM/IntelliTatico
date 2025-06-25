from pathlib import Path
import streamlit as st

from event_detection import fetch_critical_events, search_match_id
from pipelines.video_pipeline import VideoPipeline


def main() -> None:
    st.title("IntelliTatico")
    home_team = st.text_input("Home team")
    away_team = st.text_input("Away team")
    video_path = st.file_uploader("Upload full match video")

    if st.button("Process") and home_team and away_team and video_path is not None:
        match_id = search_match_id(home_team, away_team)
        if match_id is None:
            st.error("Match not found")
            return
        events = fetch_critical_events(match_id)
        pipeline = VideoPipeline(output_dir=Path("outputs"))
        clips = pipeline.process_events(Path(video_path.name), events)
        st.write(f"Generated {len(clips)} clips")
        for clip in clips:
            st.video(str(clip))


if __name__ == "__main__":
    main()
