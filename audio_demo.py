import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

def main():
    st.title("Speech-to-Text with WebRTC")

    # Define the WebRTC component
    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SENDRECEIVE,
        audio_receiver=True,
        video_receiver=False,
    )

    # Handle audio stream
    if webrtc_ctx.audio_receiver:
        st.audio(webrtc_ctx.audio_receiver.audio_bytes, format='audio/wav')

if __name__ == "__main__":
    main()
