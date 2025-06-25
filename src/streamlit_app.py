from pathlib import Path
import streamlit as st

from event_detection import fetch_critical_events
from pipelines.video_pipeline import VideoPipeline
from services.sofascscore import SofaScoreClient


def main() -> None:
    st.title("IntelliTatico")

    home_team = st.text_input("Home team")
    away_team = st.text_input("Away team")

    match_id = st.session_state.get("match_id")
    if st.button("Find match") and home_team and away_team:
        client = SofaScoreClient()
        found = client.search_match(home_team, away_team)
        if found:
            st.session_state["match_id"] = found
            match_id = found
            st.success(f"Found match ID: {found}")
        else:
            st.error("Match not found")

    st.write(f"Selected match ID: {match_id if match_id else 'None'}")
    video_path = st.file_uploader("Upload full match video")

    if st.button("Process") and match_id and video_path is not None:
        events = fetch_critical_events(int(match_id))
        pipeline = VideoPipeline(output_dir=Path("outputs"))
        clips = pipeline.process_events(Path(video_path.name), events)
        st.write(f"Generated {len(clips)} clips")
        for clip in clips:
            st.video(str(clip))


if __name__ == "__main__":
    main()
