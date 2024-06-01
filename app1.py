import pyttsx3

engine = pyttsx3.init()

speech_speed = 120  # Default speech speed (words per minute)
volume = 1.0  # Volume level (0.0 to 1.0)

voices = engine.getProperty('voices')

def list_voices():
    for idx, voice in enumerate(voices):
        print(f"{idx}: {voice.name} ({voice.languages})")

def set_voice(voice_id):
    engine.setProperty('voice', voices[voice_id].id)

if __name__ == "__main__":
    engine.setProperty('rate', speech_speed)  
    engine.setProperty('volume', volume)  

    while True:
        print("\nOptions:")
        print("1: Enter text to speak")
        print("2: List available voices")
        print("3: Set voice by ID")
        print("4: Set speech speed")
        print("5: Set volume")
        print("q: Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter what you want to say: ")
            if text.lower() == "q":
                engine.say("bye")
                engine.runAndWait()
                break
            engine.say(text)
            engine.runAndWait()
        elif choice == "2":
            list_voices()
        elif choice == "3":
            voice_id = int(input("Enter voice ID: "))
            set_voice(voice_id)
        elif choice == "4":
            speech_speed = int(input("Enter speech speed (words per minute) (Note: default is 120): "))
            engine.setProperty('rate', speech_speed)
        elif choice == "5":
            volume = float(input("Enter volume level (0.0 to 1.0) (Note: default is 1.0): "))
            engine.setProperty('volume', volume)
        elif choice.lower() == "q":
            engine.say("bye")
            engine.runAndWait()
            break
        else:
            print("Invalid option. Please try again.")