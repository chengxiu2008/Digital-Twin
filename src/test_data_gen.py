import pyttsx3
import os
import time


class TestDataGenerator:
    """
    Simulates the 'User' in the Voice VR System.
    Converts text commands into .wav audio files for testing.
    """

    def __init__(self, output_dir="tests/temp_data"):
        self.output_dir = output_dir
        # Ensure the output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_command_audio(self, text, filename="test_command.wav", rate=150):
        filepath = os.path.join(self.output_dir, filename)

        engine = pyttsx3.init()

        # --- FIX START: Force English Voice ---
        voices = engine.getProperty('voices')
        found_english = False

        for voice in voices:
            # Look for a voice that contains "en" (English) or specific names like "David"/"Zira"
            if "en_US" in voice.id or "English" in voice.name or "David" in voice.name:
                engine.setProperty('voice', voice.id)
                found_english = True
                break

        if not found_english:
            print("Warning: Could not find a specific English voice. Using default.")
        # --- FIX END ---

        engine.setProperty('rate', rate)
        engine.setProperty('volume', 1.0)

        engine.save_to_file(text, filepath)
        engine.runAndWait()

        time.sleep(0.5)
        return os.path.abspath(filepath)