from pathlib import Path
import streamlit as st

from event_detection import fetch_critical_events
from pipelines.video_pipeline import VideoPipeline


def main() -> None:
    st.title("IntelliTatico")
    match_id = st.text_input("Match ID from SofaScore")
    video_path = st.file_uploader("Upload full match video")

    if "output_dir" not in st.session_state:
        st.session_state["output_dir"] = Path("outputs")

    if st.button("Process") and match_id and video_path is not None:
        events = fetch_critical_events(int(match_id))
        pipeline = VideoPipeline(output_dir=st.session_state["output_dir"])
        clips = pipeline.process_events(Path(video_path.name), events)
        st.write(f"Generated {len(clips)} clips")
        for clip in clips:
            st.video(str(clip))


if __name__ == "__main__":
    main()
