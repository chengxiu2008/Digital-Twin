from src.test_data_gen import TestDataGenerator
from src.audio_processor import AudioProcessor
import os


def run_integration_test():
    # 1. Initialize Modules
    gen = TestDataGenerator()
    ear = AudioProcessor()

    # 2. Generate Data (User Voice)
    # We use the english voice we fixed earlier
    print("\n[Step 1] Generating Audio...")
    wav_path = gen.generate_command_audio("Computer, set brightness to 50", "asr_test.wav")

    # 3. Transcribe Data (ASR)
    print(f"\n[Step 2] Transcribing File: {wav_path}")
    text = ear.transcribe_audio(wav_path)

    # 4. Verify
    print(f"\n[Step 3] Verification")
    print(f"Expected: 'computer set brightness to 50'")
    print(f"Actual:   '{text}'")

    if "50" in text and "brightness" in text:
        print("✅ SUCCESS: ASR pipeline is working.")
    else:
        print("❌ FAILURE: Transcription mismatch.")


if __name__ == "__main__":
    run_integration_test()