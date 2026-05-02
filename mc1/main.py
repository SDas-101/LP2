import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext

from chatbot import get_response


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    chat_box.insert(tk.END, f"Bot: {text}\n")
    chat_box.see(tk.END)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        status_label.config(text="Listening...")
        root.update()

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        chat_box.insert(tk.END, f"You: {text}\n")
        chat_box.see(tk.END)
        return text

    except Exception:
        chat_box.insert(tk.END, "Voice not clear. Use text input.\n")
        chat_box.see(tk.END)
        return ""


def voice_input():
    user_input = listen()

    if user_input:
        reply = get_response(user_input)
        speak(reply)

        if user_input.lower() in ["bye", "exit", "thanks", "thank you"]:
            root.quit()

    status_label.config(text="Ready")


def send_text():
    user_input = entry.get()

    if not user_input:
        return

    chat_box.insert(tk.END, f"You: {user_input}\n")
    chat_box.see(tk.END)

    reply = get_response(user_input)
    speak(reply)

    entry.delete(0, tk.END)

    if user_input.lower() in ["bye", "exit", "thanks", "thank you"]:
        root.quit()


root = tk.Tk()
root.title("Voice Chatbot UI")
root.geometry("700x500")


chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


entry = tk.Entry(root, font=("Arial", 12))
entry.pack(fill=tk.X, padx=10, pady=5)


button_frame = tk.Frame(root)
button_frame.pack()


tk.Button(button_frame, text="Send Text", command=send_text, font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

tk.Button(button_frame, text="Speak", command=voice_input, font=("Arial", 12)).pack(side=tk.LEFT, padx=5)


status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack(pady=5)


root.mainloop()