import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load your audio file (supports WAV, AIFF, FLAC)
audio_file = "speech_test.wav"  # Replace with your file path

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
