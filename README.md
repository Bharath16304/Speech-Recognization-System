# 🎤 Speech-to-Text (STT) System

A simple Python-based Speech Recognition Tool that converts short audio clips into text using pre-trained models and libraries like `SpeechRecognition` and `Wav2Vec 2.0`.

---

## 🚀 Features

✅ Transcribe `.wav` audio files into text  
✅ Online transcription using Google's Speech-to-Text API (via `SpeechRecognition`)  
✅ Offline, high-accuracy transcription using `Wav2Vec 2.0` (Hugging Face Transformers)  
✅ Automatic resampling for proper audio formats  
✅ Easy to use and extend  

---

## 🛠️ Requirements

Ensure you have Python installed. Then, install the required dependencies:

pip install SpeechRecognition pydub torch torchaudio transformers


📂 Usage
Clone or download this repository.

Place your audio file in the project directory (.wav format recommended).

Run one of the provided Python scripts:

Using SpeechRecognition (Online, Simple):
python stt_speech_recognition.py

Using Wav2Vec 2.0 (Offline, Advanced):
python stt_wav2vec2.py
Example inside stt_speech_recognition.py:
audio_file = "audio.wav"  # Replace with your file
text = transcribe_audio(audio_file)
print("Transcription:", text)


🔧 How It Works
SpeechRecognition:
Uses Google Web Speech API to convert audio to text (requires internet connection).

Wav2Vec 2.0 (Hugging Face):
Loads Facebook's pre-trained wav2vec2-base-960h model to perform transcription offline.
Works best with mono-channel, 16kHz .wav audio files (resampling included).

📦 Example Output
Original Audio:
"Hello, welcome to the Speech-to-Text system."

Transcribed Text:
Hello, welcome to the Speech-to-Text system.

💡 Future Improvements
Support for multiple languages

Noise filtering and audio enhancement

Batch transcription for multiple audio files

Integration with GUI or web interfaces

Real-time speech recognition
