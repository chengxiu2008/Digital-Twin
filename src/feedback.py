import pyttsx3
import threading


class SystemVoice:
    """
    The System's 'Mouth'.
    Provides audio confirmation after the 'Hands' finish their job.
    """

    def __init__(self):
        # We initialize the engine only when needed to avoid locking
        pass

    def speak(self, text):
        """
        Runs speech in a separate thread so it doesn't block the testing logic.
        """
        print(f"🔊 [System Voice]: {text}")

        # Threading is crucial here!
        # Otherwise, your test waits for the robot to finish talking before asserting.
        thread = threading.Thread(target=self._run_speech, args=(text,))
        thread.start()

    def _run_speech(self, text):
        try:
            # Re-init engine inside thread for OS compatibility
            engine = pyttsx3.init()

            # --- FIX: Force English Voice (Again) ---
            voices = engine.getProperty('voices')
            for voice in voices:
                # Look for English identifiers common on Windows/Mac
                if "en_US" in voice.id or "English" in voice.name or "David" in voice.name or "Zira" in voice.name:
                    engine.setProperty('voice', voice.id)
                    break
            # ----------------------------------------

            # Make the system sound authoritative (slightly faster)
            engine.setProperty('rate', 170)

            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"[Voice Error] Could not speak: {e}")