# Voice-Controlled IoT Digital Twin

**A Full-Stack Hardware-in-the-Loop (HIL) Simulation Framework**

## Project Overview
This project serves as a **Digital Twin** for a voice-activated IoT device. It simulates the complete signal chain of a modern smart device—from audio stimulus generation to hardware actuation—completely in software.

Designed to demonstrate **Automated Embedded Testing** capabilities, this framework decouples hardware dependencies, allowing for scalable **CI/CD integration** while maintaining real-world fidelity through hardware abstraction layers (HAL).

---

## Architecture: The "Anatomy" of the System

The system is architected to mimic the biological subsystems of a smart assistant:

| Component | Biological Equiv. | Technical Implementation | Function |
| :--- | :--- | :--- | :--- |
| **Test Data Gen** | **User Mouth** | `pyttsx3` (TTS Engine) | Generates synthetic `.wav` audio artifacts for deterministic testing. |
| **Audio Processor** | **System Ear** | `SpeechRecognition` (Google API) | Handles ASR (Automated Speech Recognition) and signal processing. |
| **NLU Parser** | **System Brain** | `Regex` / Python Logic | Extracts Intents (`SET_BRIGHTNESS`) and Slots (`50`) from raw text. |
| **System Controller** | **System Hands** | `screen_brightness_control` | **HAL (Hardware Abstraction Layer)** that actuates physical laptop hardware. |
| **Feedback Module** | **System Mouth** | `pyttsx3` (System Voice) | Provides VUI (Voice User Interface) audio feedback upon execution. |

---

## Key Features

* **End-to-End Simulation:** Tests the full loop: `Text -> Audio File -> ASR -> NLU -> Logic -> Hardware Change -> Audio Feedback`.
* **Hardware-in-the-Loop (HIL):** Controls actual physical hardware (Laptop Screen Brightness) to verify driver execution.
* **Robustness & Safety:** Implements **Input Clamping** (Saturation) in the firmware logic to handle out-of-bounds values (e.g., clamping 150% brightness to 100%) without crashing.
* **CI/CD Ready:** The "Mouth" and "Ear" modules are environment-aware. They function in **Headless Mode** during automated pipeline runs (no speakers/mic required) and **Live Mode** for demos.

---

## Installation

**Prerequisites:** Python 3.8+

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/voice-iot-simulator.git](https://github.com/your-username/voice-iot-simulator.git)
    cd voice-iot-simulator
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Dependencies include: `pytest`, `pyttsx3`, `SpeechRecognition`, `screen_brightness_control`, `pyaudio`)*

---

## Usage

### 1. The Full Body Simulation (Demo)
Run the end-to-end simulation where the system generates its own audio commands and reacts to them.
```bash
python final_demo.py
