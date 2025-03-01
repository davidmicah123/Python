# import tkinter as tk
# import speech_recognition as sr

# # Function to convert speech to text
# def recognize_speech():
#     recognizer = sr.Recognizer()  # Create a Recognizer instance
#     with sr.Microphone() as source:
#         print("Listening...")  # Optional: print to console
#         audio = recognizer.listen(source)  # Listen for audio input

#     try:
#         # Recognize speech using Google Web Speech API
#         text = recognizer.recognize_google(audio)
#         text_output.delete("1.0", tk.END)  # Clear previous text
#         text_output.insert(tk.END, text)  # Insert recognized text
#     except sr.UnknownValueError:
#         text_output.delete("1.0", tk.END)
#         text_output.insert(tk.END, "Sorry, I could not understand the audio.")
#     except sr.RequestError:
#         text_output.delete("1.0", tk.END)
#         text_output.insert(tk.END, "Could not request results from Google Speech Recognition service.")

# # Create the main window
# root = tk.Tk()
# root.title("Speech to Text Converter")

# # Create a Button to trigger the speech recognition
# recognize_button = tk.Button(root, text="Recognize Speech", command=recognize_speech)
# recognize_button.pack(pady=10)

# # Create a Text widget to display the recognized text
# text_output = tk.Text(root, height=10, width=50)
# text_output.pack(pady=10)

# # Run the application
# root.mainloop()


import tkinter as tk
import pyttsx3

# Function to convert text to speech
def speak():
    text = text_entry.get("1.0", tk.END)  # Get the text from the text box
    if text.strip():  # Check if the text is not empty
        engine.say(text)
        engine.runAndWait()
    else:
        print("Please enter some text.")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create the main window
root = tk.Tk()
root.title("Text to Speech Converter")

# Create a Text widget for user input
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Create a Button to trigger the speech
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack(pady=10)

# Run the application
root.mainloop()