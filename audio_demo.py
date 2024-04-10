import streamlit as st
from streamlit_mic_recorder import mic_recorder

def main():
    st.title('abc')
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

def handle_recording(recording):
    if recording:
        st.write("Recording...")
    else:
        st.write("Recording stopped. Text: {}".format(get_text_from_audio()))

def get_text_from_audio():
    # Function to process the recorded audio and extract text
    # This function should return the extracted text from the audio
    return "Example extracted text"

if __name__ == "__main__":
    main()
