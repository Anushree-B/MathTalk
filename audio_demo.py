import streamlit as st
from streamlit_mic_recorder import mic_recorder

# def main():
#     st.title('abc')
#     audio = mic_recorder(
#         start_prompt="Start recording",
#         stop_prompt="Stop recording",
#         just_once=False,
#         use_container_width=False,
#         callback=None,
#         args=(),
#         kwargs={},
#         key=None
#     )

# def handle_recording(recording):
#     if recording:
#         st.write("Recording...")
#     else:
#         st.write("Recording stopped. Text: {}".format(get_text_from_audio()))

# def get_text_from_audio():
#     # Function to process the recorded audio and extract text
    # This function should return the extracted text from the audio
#     return "Example extracted text"

# if __name__ == "__main__":
#     main()

# import streamlit as st
# from streamlit_mic_recorder import mic_recorder
# import speech_recognition as sr

# def main():
#     st.title('Speech-to-Text with Streamlit')

#     audio = mic_recorder(
#         start_prompt="Start recording",
#         stop_prompt="Stop recording",
#         just_once=True,
#     )

#     if audio is not None:
#         # Transcribe audio to text
#         text = transcribe_audio(audio)
#         st.write("Recorded Text:", text)

# def transcribe_audio(audio_file):
#     # Transcribe audio to text
#     r = sr.Recognizer()
#     try:
#         with sr.AudioFile(audio_file) as source:
#             audio_data = r.record(source)
    #     text = r.recognize_google(audio_data)
    #     return text
    # except sr.UnknownValueError:
    #     st.write("Unable to recognize speech")
    #     return ""
    # except sr.RequestError as e:
    #     st.write("Error fetching results from Google Speech Recognition service; {0}".format(e))
#         return ""

# if __name__ == "__main__":
#     main()

import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import tempfile

def main():
    st.title('Speech-to-Text with Streamlit')

    with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
        audio = mic_recorder(
            start_prompt="Start recording",
            stop_prompt="Stop recording",
            just_once=True,
            output_filename=temp_audio_file.name
        )

    if audio is not None:
        # Transcribe audio to text
        text = transcribe_audio(audio)
        st.write("Recorded Text:", text)

def transcribe_audio(audio_file):
    # Transcribe audio to text
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        st.write("Unable to recognize speech")
        return ""
    except sr.RequestError as e:
        st.write("Error fetching results from Google Speech Recognition service; {0}".format(e))
        return ""

if __name__ == "__main__":
    main()
