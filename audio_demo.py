import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
    r = sr.Recognizer()
    st.write("Recognizer called")
    audio_file_path = "temp_audio_file.wav"
    with open(audio_file_path, "wb") as f:
        f.write(audio.export().read())
    with sr.AudioFile(audio_file_path) as source:
        audio_text = r.listen(source)
        st.write("audio text recorded")
