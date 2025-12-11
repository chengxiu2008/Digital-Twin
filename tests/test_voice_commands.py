import time
import pytest
from src.system_controller import SystemController

def parse_voice_command(audio_text):
    if 'brightness' in audio_text:
        import re
        percent = re.findall(r'\d+', audio_text)
        if percent:
            return int(percent[0])
    return None

test_scenarios = [
    ('set brightness to 50', 50),
    ('maximum brightness to 100', 100),
    ('set brightness to 0', 0),
    ('set brightness to 25', 25),
    ('set brightness to 75', 75),
    ('please change brightness to 60', 60),
]

@pytest.mark.parametrize('command_text, expected_percent', test_scenarios)
def test_brightness_command(command_text, expected_percent):
    # Test brightness command
    print(f"\n------- Testing Scenario: '{command_text}'----")
    system_controller = SystemController()
    voice_percent = parse_voice_command(command_text)
    system_controller.set_brightness(voice_percent)
    time.sleep(1)
    current_percent = system_controller.get_brightness()
    assert current_percent == [expected_percent, expected_percent]