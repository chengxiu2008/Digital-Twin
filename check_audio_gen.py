from src.test_data_gen import TestDataGenerator
import os

print("--- 1. Initializing Generator ---")
gen = TestDataGenerator()

print("--- 2. Generating Audio ---")
file_path = gen.generate_command_audio("Computer, set brightness to 50", "sanity_check.wav")

print(f"--- 3. Checking File ---")
if os.path.exists(file_path):
    print(f"SUCCESS: Audio file created at: {file_path}")
    print(f"File Size: {os.path.getsize(file_path)} bytes")
else:
    print("FAILURE: File was not created.")