from src.test_data_gen import TestDataGenerator
from src.audio_processor import AudioProcessor
from src.nlu_parser import parse_voice_command
from src.system_controller import SystemController
import time


def run_e2e_test():
    print("=== STARTING E2E VOICE TEST ===")

    # 1. Initialize Components
    gen = TestDataGenerator()
    ear = AudioProcessor()
    brain = SystemController()

    # 2. Define Test Case
    target_value = 60
    command_text = f"Computer, please set brightness to {target_value}"

    # 3. Execution Pipeline

    # Node 1: User Voice
    print(f"\n[1] User speaks: '{command_text}'")
    wav_path = gen.generate_command_audio(command_text, "full_chain_test.wav")

    # Node 2: ASR
    print(f"[2] ASR Processing...")
    transcribed_text = ear.transcribe_audio(wav_path)
    print(f"    -> Heard: '{transcribed_text}'")

    # Node 3: NLU
    print(f"[3] NLU Parsing...")
    intent = parse_voice_command(transcribed_text, wake_word="computer")
    print(f"    -> Intent: {intent}")

    # Node 4: Logic & Hardware
    if intent:
        print(f"[4] Executing Logic...")
        success = brain.execute_command(intent)

        # Node 5: Verification (The Test Assertion)
        time.sleep(1)  # Wait for hardware
        current_val = brain.get_current_status()

        print(f"\n[5] Verification")
        print(f"    Target: {target_value}")
        print(f"    Actual: {current_val}")

        # Allow 5% tolerance for hardware quirks
        if abs(current_val - target_value) <= 5:
            print("✅ TEST PASSED: Hardware state matches voice command.")
        else:
            print("❌ TEST FAILED: Hardware did not update correctly.")
    else:
        print("❌ TEST FAILED: NLU failed to understand command.")


if __name__ == "__main__":
    run_e2e_test()