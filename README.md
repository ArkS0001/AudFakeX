# AudFake-Group-B
team discuss
![browserpreview_tmp-1](https://github.com/ArkS0001/AudFake-Group-B/assets/113760964/c729d14b-ceb4-4e93-8ce9-85db9082e82c)

![image_processing20191008-24660-1greu2y](https://github.com/ArkS0001/AudFake-Group-B/assets/113760964/7284edbb-8e9f-43c7-9c7c-b226bdd2762a)


https://github.com/CorentinJ/Real-Time-Voice-Cloning

https://github.com/smoke-trees/Voice-synthesis

https://github.com/Suhee05/Text-Independent-Speaker-Verification

https://github.com/kingridda/voice-cloning-AI

https://github.com/PaddlePaddle/PaddleSpeech

https://github.com/jackaduma/CycleGAN-VC2

https://github.com/deterministic-algorithms-lab/Cross-Lingual-Voice-Cloning

https://github.com/jackaduma/CycleGAN-VC2

https://github.com/ming024/FastSpeech2 ------>IMP LINK



To achieve real-time audio processing in Python, you can use libraries such as PyAudio for audio input/output and SpeechRecognition for speech-to-text conversion. Below is a simple example of how you could implement the real-time processing part of converting one audio to another voice using a different voice in real-time:

    
    import speech_recognition as sr
    import pyttsx3
    
    # Initialize the speech recognition engine
    recognizer = sr.Recognizer()
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set the properties for the text-to-speech engine (e.g., voice)
    voices = engine.getProperty('voices')
    # You can choose a different voice here, e.g., voices[1] for a different voice
    engine.setProperty('voice', voices[0].id)
    
    # Function to process audio in real-time
    def process_audio():
        with sr.Microphone() as source:
            print("Say something...")
            while True:
                try:
                    audio_data = recognizer.listen(source, timeout=None)
                    text = recognizer.recognize_google(audio_data)
                    print("You said:", text)
                    
                    # Convert text to speech with a different voice
                    engine.say(text)
                    engine.runAndWait()
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Error retrieving speech recognition results; {0}".format(e))
    
    # Call the function to start real-time processing
    process_audio()

In this code:

  We use SpeechRecognition library to capture audio from the microphone in real-time and convert it to text using Google's speech recognition service.
  We use pyttsx3 library to convert the recognized text into speech with a different voice (you can change the voice by selecting a different index from the voices list).
  The process_audio() function continuously listens to audio from the microphone, recognizes speech, converts it to text, and then synthesizes the text into speech with a different voice.

Ensure you have installed both SpeechRecognition and pyttsx3 libraries via pip before running the code:

    pip install SpeechRecognition pyttsx3

This code provides a basic framework for real-time audio processing in Python. Depending on your specific requirements and use case, you may need to add additional functionalities or optimizations.
