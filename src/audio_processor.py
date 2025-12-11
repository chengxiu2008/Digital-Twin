import speech_recognition as sr
import os


class AudioProcessor:
    """
    Simulates the ASR (Automatic Speech Recognition) component.
    Converts audio files (.wav) into text.
    """

    def __init__(self):
        # The Recognizer is the core engine
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_file_path):
        """
        Reads a WAV file and returns the transcribed text.

        Args:
            audio_file_path (str): Path to the .wav file

        Returns:
            str: The text heard (lowercase), or empty string if failed.
        """
        if not os.path.exists(audio_file_path):
            print(f"[ASR Error] File not found: {audio_file_path}")
            return ""

        # Open the file (Simulating reading from a microphone buffer)
        with sr.AudioFile(audio_file_path) as source:
            # Optional: Simulate 'SSE' (Signal enhancement) by adjusting for ambient noise
            # self.recognizer.adjust_for_ambient_noise(source)

            # Read the entire file
            audio_data = self.recognizer.record(source)

            try:
                # We use Google Web Speech API (Free, requires internet)
                # In a real Motorola/Zebra device, this would be a custom model
                print(f"--- [ASR] Sending audio to Cloud Model... ---")
                text = self.recognizer.recognize_google(audio_data)

                print(f"--- [ASR] Result: '{text}' ---")
                return text.lower()

            except sr.UnknownValueError:
                print("[ASR Error] Model could not understand the audio.")
                return ""
            except sr.RequestError as e:
                print(f"[ASR Error] API Unreachable: {e}")
                return ""