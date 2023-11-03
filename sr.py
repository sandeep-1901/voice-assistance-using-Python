import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

# Define the function to speak text
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

# Define the voice assistant function
def voice_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Web Speech API
        command = recognizer.recognize_google(audio)
        print("You said: " + command)

        # Basic commands
        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "what is the time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The current time is " + time)
        elif "open website" in command:
            website = command.split()[-1]
            webbrowser.open("https://www." + website)
        else:
            speak("Sorry, I didn't understand that.")

    except sr.UnknownValueError:
        speak("I didn't hear anything. Please try again.")
    except sr.RequestError as e:
        speak("I'm sorry, but I couldn't request results; {0}".format(e))

# Start the voice assistant
while True:
    voice_assistant()
