from gtts import gTTS
from gtts.lang import tts_langs
import pygame
import tempfile

# Initialize pygame for audio playback
pygame.init()

SUPPORTED_LANGUAGES = tts_langs()

def list_languages():
    print("Available languages:")
    for lang, name in SUPPORTED_LANGUAGES.items():
        print(f"{name}: {lang}")

def play_audio(file_path):
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    while pygame.mixer.get_busy():  # Wait until speech is completed
        pygame.time.Clock().tick(10)

def text_to_speech(text, language_code):
    tts = gTTS(text=text, lang=language_code)
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(fp.name + ".mp3")
        play_audio(fp.name + ".mp3")

if __name__ == "__main__":
    # Default language
    language_code = 'en'

    while True:
        print("\nOptions:")
        print("1: Enter text to speak")
        print("2: List available languages")
        print("3: Set language")
        print("q: Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter what you want to say: ")
            text_to_speech(text, language_code)
        elif choice == "2":
            list_languages()
        elif choice == "3":
            new_language_code = input("Enter language code (e.g., 'en', 'es'): ")
            if new_language_code in SUPPORTED_LANGUAGES:  # Check if language code is valid
                language_code = new_language_code
                print(f"Language '{SUPPORTED_LANGUAGES[language_code]}' is set successfully.")
            else:
                print("Invalid language code. Language not changed.")
        elif choice.lower() == "q":
            text_to_speech("Goodbye", language_code)
            break
        else:
            print("Invalid option. Please try again.")

    # Quit pygame
    pygame.quit()
