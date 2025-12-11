import re


def parse_voice_command(text, wake_word="computer"):
    """
    Simulates the NLU (Natural Language Understanding) component.
    Extracts INTENT and SLOTS from raw text.

    Args:
        text (str): Raw text from ASR (e.g. "computer set brightness to 50")
        wake_word (str): Security check word

    Returns:
        dict: Structured command (e.g. {'action': 'set_brightness', 'value': 50})
        None: If command is invalid or wake word missing
    """
    if not text:
        return None

    # Normalize input
    text = text.lower()

    # 1. Wake Word Check (Security Layer)
    if wake_word not in text:
        print(f"[NLU] Ignored: Wake word '{wake_word}' missing.")
        return None

    # 2. Intent Classification: "Set Brightness"
    if "brightness" in text:
        # 3. Slot Filling: Extract the number
        numbers = re.findall(r'\d+', text)
        if numbers:
            return {
                "action": "set_brightness",
                "value": int(numbers[0])  # Convert "50" string to 50 int
            }
        else:
            print("[NLU] Intent recognized, but missing value slot.")
            return None

    # Add more intents here later (e.g., "volume", "turn off")

    print("[NLU] Text recognized, but no matching intent found.")
    return None