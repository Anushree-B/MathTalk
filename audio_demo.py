import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

def main():
    st.title("List Available Audio Devices")

    # JavaScript code to enumerate audio devices
    js_code = """
    <script>
    navigator.mediaDevices.enumerateDevices().then(devices => {
        const audioDevices = devices.filter(device => device.kind === 'audioinput');
        const audioDeviceNames = audioDevices.map(device => device.label);
        const audioDeviceIds = audioDevices.map(device => device.deviceId);
        const audioDevicesList = document.createElement('ul');
        audioDeviceNames.forEach((name, index) => {
            const listItem = document.createElement('li');
            listItem.textContent = `${name} (ID: ${audioDeviceIds[index]})`;
            audioDevicesList.appendChild(listItem);
        });
        document.body.appendChild(audioDevicesList);
    });
    </script>
    """

    # Display the JavaScript code
    st.write(js_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



# def main():
#     st.title("Speech-to-Text with WebRTC")

#     # Define the WebRTC component
#     webrtc_ctx = webrtc_streamer(
#         key="speech-to-text",
#         mode=WebRtcMode.SENDRECEIVE,
#         audio_receiver=True,
#         video_receiver=False,
#     )

#     # Handle audio stream
#     if webrtc_ctx.audio_receiver:
#         st.audio(webrtc_ctx.audio_receiver.audio_bytes, format='audio/wav')

# if __name__ == "__main__":
#     main()
