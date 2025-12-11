import screen_brightness_control as sbc
from src.feedback import SystemVoice

class SystemController:
    """
    The Main Controller Logic (The 'Brain').
    Decides HOW to execute the command on hardware.
    """

    def __init__(self):
        self.voice = SystemVoice()  # <-- Connect the Mouth

    def execute_command(self, command_dict):
        """
        Takes structured NLU output and routes it to hardware.
        """
        if not command_dict:
            return False

        action = command_dict.get('action')
        value = command_dict.get('value')

        if action == "set_brightness":
            return self._set_brightness_logic(value)

        print(f"[Controller] Unknown action: {action}")
        return False

    def _set_brightness_logic(self, level):
        """
        Contains Business Logic (Clamping, validation, etc.)
        """
        # Logic Rule 1: Input Clamping (Firmware Protection)
        safe_level = max(0, min(level, 100))

        if safe_level != level:
            print(f"[Logic] Clamping input {level} to {safe_level}")

        try:
            print(f"--- [Hardware] Setting Brightness to {safe_level}% ---")
            # In a real interview, you can comment this out if you don't want screen flashing
            sbc.set_brightness(safe_level)

            # 3. The System Mouth (Feedback)
            # This is the VUI (Voice User Interface) loop
            self.voice.speak(f"OK. Brightness set to {safe_level}.")

            return True
        except Exception as e:
            print(f"[Hardware Error] {e}")
            self.voice.speak("I'm sorry, I can't control the screen.")
            return False

    def get_current_status(self):
        try:
            return sbc.get_brightness()[0]
        except:
            return 0