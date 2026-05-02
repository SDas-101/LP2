# Voice Chatbot with Speech and GUI

## Overview

This project implements a simple rule-based voice chatbot with a graphical user interface.
It supports both text input and voice input, and responds using text-to-speech.

The chatbot handles basic customer service queries such as:

* Order status
* Refunds and cancellations
* Payment issues
* Delivery information
* Product inquiries

The system combines:

* Speech recognition (microphone input)
* Text-to-speech output
* A Tkinter-based GUI

---

## Features

* Voice input using microphone
* Text input via GUI
* Spoken responses using TTS
* Rule-based chatbot logic
* Simple and lightweight UI

---

## Project Structure

```
mc1/
├── main.py            # Main GUI + voice chatbot app
├── chatbot.py         # Rule-based response logic
├── mic_test.py        # Test microphone input
├── speaker_test.py    # Test speaker output
├── output.pdf         # Sample UI output (optional)
├── tempbot/           # Experimental folder (optional / unused)
```

---

## Requirements

Install dependencies using:

```
pip install speechrecognition pyttsx3 pyaudio
```

### Important Notes

* `pyaudio` installation may fail on Windows. Use:

  ```
  pip install pipwin
  pipwin install pyaudio
  ```
* Ensure your microphone is properly connected.
* Internet is required for speech recognition (Google API).

---

## How to Run

### Step 1: Run the main application

```
python main.py
```

### Step 2: Use the interface

* Type a message and click **Send Text**
* OR click **Speak** and talk into your microphone

The chatbot will respond both in text and voice.

---

## Testing Individual Components

### Microphone Test

```
python mic_test.py
```

### Speaker Test

```
python speaker_test.py
```

---

## How It Works

### Chatbot Logic

The chatbot uses simple keyword matching to generate responses.
Defined in:

* `chatbot.py` → `get_response()` 

### Main Application

The GUI and voice pipeline are handled in:

* `main.py` 

Flow:

1. Capture input (text or voice)
2. Convert speech to text (if needed)
3. Generate response
4. Display and speak output

---

## Example Interaction

* User: "Where is my order?"
* Bot: "Your order is currently being processed..."

---

## Notes

* This is a rule-based chatbot (no ML involved)
* Responses are fixed and keyword-driven
* Can be extended with NLP or ML models

---

## Future Improvements

* Add NLP-based intent detection
* Improve UI design
* Add conversation memory
* Integrate with APIs for real-time data

---

## License

For academic and learning purposes.
