from src.test_data_gen import TestDataGenerator
from src.audio_processor import AudioProcessor
from src.nlu_parser import parse_voice_command
from src.system_controller import SystemController
import time


def run_full_body_simulation():
    print("=== FULL BODY IOT SIMULATION  ===")

    # 1. Wake up the Organs
    user_mouth = TestDataGenerator()
    system_ear = AudioProcessor()
    system_body = SystemController()  # Contains Brain, Hands, and System Mouth

    # 2. Define the Command
    # Let's try a tricky one that needs Clamping (Logic)
    command_text = "Computer, set brightness to 150"

    # --- PHASE 1: STIMULUS ---
    print(f"\n[1] User Says: '{command_text}'")
    wav_path = user_mouth.generate_command_audio(command_text, "demo.wav")

    # --- PHASE 2: PERCEPTION ---
    print(f"[2] System Hearing...")
    transcribed_text = system_ear.transcribe_audio(wav_path)
    print(f"    -> Heard: '{transcribed_text}'")

    # --- PHASE 3: COGNITION ---
    print(f"[3] System Thinking...")
    intent = parse_voice_command(transcribed_text, wake_word="computer")

    # --- PHASE 4: ACTION ---
    if intent:
        print(f"[4] System Acting...")
        # This will trigger the Hands (Screen) AND the Mouth ("OK...")
        system_body.execute_command(intent)

        # Wait for the speech to finish
        time.sleep(3)

        # --- PHASE 5: VERIFICATION ---
        current_val = system_body.get_current_status()
        print(f"\n[5] Final Verification")
        print(f"    Requested: 150")
        print(f"    Clamped To: 100")
        print(f"    Actual Hardware: {current_val}")

        if current_val == 100:
            print("SUCCESS: Full loop complete.")
    else:
        print("FAILED: Could not understand command.")


if __name__ == "__main__":
    run_full_body_simulation()