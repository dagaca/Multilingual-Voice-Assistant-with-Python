import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
from deep_translator import GoogleTranslator

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today is {current_date}."

def translate():
    speak("Hangi metni çevirmemi istersiniz?")
    text_query = listen()

    try:
        translate_text = GoogleTranslator(source='en', target='tr').translate(text_query)

        print(f"Translated Text: {translate_text}")
        speak(f"Translated Text: {translate_text}")

    except Exception as e:
        print(f"An error occurred during translation: {e}")
        speak("An error occurred during translation. Please try again.")
        
def get_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
        return f"Multiple results found. Please specify your query. Options: {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        return f"Sorry, I could not find any information about '{query}' on Wikipedia."
    except wikipedia.exceptions.WikipediaException as e:
        return f"An error occurred: {e}"

def open_website(query):
    base_url = "https://www."
    end_url = ".com/"

    formatted_query = query.lower().replace(' ', '-')

    full_url = f"{base_url}{formatted_query}{end_url}"

    speak(f"Opening {full_url} in your default web browser.")
    webbrowser.open(full_url)

def play_music():
    speak("Sure, what music would you like to listen to?")
    music_query = listen()

    search_url = f"https://www.youtube.com/results?search_query={music_query.replace(' ', '+')}"

    webbrowser.open(search_url)

    return f"Searching for {music_query} on YouTube. Please select a video to play."

def write_note():
    speak("What should I write, sir?")
    note = ""

    while True:
        user_input = listen()
        note += user_input + " "
        print(f"Current Note: {note}")

        if "exit" in note.lower():
            break

    note = note.lower().replace("note save", "").strip()

    file = open('notes.txt', 'a')
    file.write(f"{note}\n")
    speak("Note saved.")

    file.close()