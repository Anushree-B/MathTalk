import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr
import io
from pydub import AudioSegment

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read(), format='audio/wav')  

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
    
    # Export the audio to a bytes buffer
    audio_bytes = audio.export().read()
    
    # Check if the audio_bytes is not empty
    if audio_bytes:
        st.write("Audio successfully saved in bytes buffer.")
        
        try:
            # Initialize recognizer
            r = sr.Recognizer()
            st.write("Recognizer called")
            
            # Convert audio bytes to AudioSegment
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            
            # Export AudioSegment to a WAV format bytes buffer
            wav_buffer = io.BytesIO()
            audio_segment.export(wav_buffer, format='wav')
            wav_buffer.seek(0)
            
            # Use the wav buffer with speech recognition
            with sr.AudioFile(wav_buffer) as source:
                audio_text = r.record(source)
                st.write("Audio text recorded")

                # Recognize speech using Google Speech Recognition
                text = r.recognize_google(audio_text)
                st.write("Recognized Text:", text)

        except Exception as e:
            st.write("Error during speech recognition:", e)
    else:
        st.write("Failed to save the audio to bytes buffer.")
else:
    st.write("No audio recorded.")
