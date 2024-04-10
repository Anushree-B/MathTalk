import streamlit as st
import pyaudio
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from streamlit_mic_recorder import mic_recorder

def main():
    audio = mic_recorder(
        start_prompt="Start recording",
        stop_prompt="Stop recording",
        just_once=False,
        use_container_width=False,
        callback=None,
        args=(),
        kwargs={},
        key=None
    )

if __name__ == "__main__":
    main()