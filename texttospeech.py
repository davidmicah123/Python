# # # import tkinter as tk
# # # import speech_recognition as sr

# # # # Function to convert speech to text
# # # def recognize_speech():
# # #     recognizer = sr.Recognizer()  # Create a Recognizer instance
# # #     with sr.Microphone() as source:
# # #         print("Listening...")  # Optional: print to console
# # #         audio = recognizer.listen(source)  # Listen for audio input

# # #     try:
# # #         # Recognize speech using Google Web Speech API
# # #         text = recognizer.recognize_google(audio)
# # #         text_output.delete("1.0", tk.END)  # Clear previous text
# # #         text_output.insert(tk.END, text)  # Insert recognized text
# # #     except sr.UnknownValueError:
# # #         text_output.delete("1.0", tk.END)
# # #         text_output.insert(tk.END, "Sorry, I could not understand the audio.")
# # #     except sr.RequestError:
# # #         text_output.delete("1.0", tk.END)
# # #         text_output.insert(tk.END, "Could not request results from Google Speech Recognition service.")

# # # # Create the main window
# # # root = tk.Tk()
# # # root.title("Speech to Text Converter")

# # # # Create a Button to trigger the speech recognition
# # # recognize_button = tk.Button(root, text="Recognize Speech", command=recognize_speech)
# # # recognize_button.pack(pady=10)

# # # # Create a Text widget to display the recognized text
# # # text_output = tk.Text(root, height=10, width=50)
# # # text_output.pack(pady=10)

# # # # Run the application
# # # root.mainloop()


# # import tkinter as tk
# # import pyttsx3

# # # Function to convert text to speech
# # def speak():
# #     text = text_entry.get("1.0", tk.END)  # Get the text from the text box
# #     if text.strip():  # Check if the text is not empty
# #         engine.say(text)
# #         engine.runAndWait()
# #     else:
# #         print("Please enter some text.")

# # # Initialize the text-to-speech engine
# # engine = pyttsx3.init()

# # # Create the main window
# # root = tk.Tk()
# # root.title("Text to Speech Converter")

# # # Create a Text widget for user input
# # text_entry = tk.Text(root, height=10, width=50)
# # text_entry.pack(pady=10)

# # # Create a Button to trigger the speech
# # speak_button = tk.Button(root, text="Speak", command=speak)
# # speak_button.pack(pady=10)

# # # Run the application
# # root.mainloop()

# # import time

# # while True:
# #     print("Active")  # Simulates activity
# #     time.sleep(60)  # Waits for 60 seconds before repeating
# # 1 


# # import time

# # file_path = "script.js"  # Writing to script.js

# # while True:
# #     with open(file_path, "a") as file:  
# #         file.write('console.log("Still active...");\n')  # JavaScript syntax
# #     print("Wrote to script.js")  
# #     time.sleep(60)  # Wait for 30 seconds before writing again


# # import time
# # import random

# # file_path = "script.js"

# # messages = [
# #     'console.log("Working on feature A...");',
# #     'console.log("Fixing bug in the login flow");',
# #     'console.log("Refactoring the API calls");',
# #     'console.log("Trying a new approach to the UI");',
# #     'console.log("Optimizing performance...");',
# #     'console.log("Checking edge cases");',
# #     'console.log("Improving error handling");',
# #     'console.log("Still here coding :)");',
# #     'console.log("Adjusting layout responsiveness");'
# # ]

# # def write_to_file():
# #     message = random.choice(messages)
# #     with open(file_path, "a") as file:
# #         file.write(message + "\n")
# #     print(f"Wrote: {message}")

# # while True:
# #     write_to_file()

# #     # Short break: simulate realistic edit intervals (45s to 3 minutes)
# #     short_pause = random.uniform(45, 180)
# #     time.sleep(short_pause)

# #     # Occasionally take a long break (like lunch or a phone call)
# #     if random.randint(1, 25) == 5:  # ~4% chance
# #         long_pause = random.randint(600, 1800)  # 10 to 30 minutes
# #         print(f"Taking a long break for {long_pause // 60} minutes")
# #         time.sleep(long_pause)


# import time
# import random

# file_path = "script.js"

# messages = [
#     '// TODO: Refactor this function',
#     'function calculateTotal(items) {\n    return items.reduce((sum, item) => sum + item.price, 0);\n}',
#     'const username = "devUser";',
#     'let count = 0;',
#     'const fruits = ["apple", "banana", "cherry"];',
#     'for (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}',
#     'if (count > 10) {\n    console.log("Too many attempts");\n}',
#     'document.querySelector("#submit").addEventListener("click", handleSubmit);',
#     'console.log("Working on feature A...");',
#     'console.log("Fixing bug in the login flow");',
#     'console.log("Refactoring the API calls");',
#     'console.log("Trying a new approach to the UI");',
#     'console.log("Optimizing performance...");',
#     'console.log("Checking edge cases");',
#     'console.log("Improving error handling");',
#     'console.log("Still here coding :)");',
#     'console.log("Adjusting layout responsiveness");',
#     'const user = {\n    name: "Alice",\n    age: 25,\n    isAdmin: false\n};',
#     'function greet(name) {\n    return `Hello, ${name}!`;\n}',
#     '// Simulate async request\nsetTimeout(() => {\n    console.log("Fetched data successfully");\n}, 1500);',
#     'const isLoggedIn = true;',
#     'let retries = 3;',
#     'while (retries > 0) {\n    console.log("Retrying...");\n    retries--;\n}',
#     '// Begin session tracking',
#     'console.log(new Date().toISOString());',
#     '// Simulate user interaction',
#     'window.addEventListener("scroll", () => {\n    console.log("User scrolled");\n});',
#     '// Temporary debugging\nconsole.debug("Debug mode ON");'
# ]

# def write_to_file():
#     message = random.choice(messages)
#     with open(file_path, "a") as file:
#         file.write(message + "\n")
#     print(f"Wrote: {message}")

# while True:
#     write_to_file()

#     # Short break: 60–90 seconds (always under 2 mins)
#     short_pause = random.uniform(60, 90)
#     time.sleep(short_pause)

#     # Optional: Long break every ~30–50 actions
#     if random.randint(1, 50) == 3:
#         long_pause = random.randint(600, 1200)
#         print(f"Taking a long break for {long_pause // 60} minutes")
#         time.sleep(long_pause)


import time
import random
from datetime import datetime, timedelta

# File priorities
files = {
    "script.js": "js",
    "logic.js": "js",
    "app.js": "js",
    "index.html": "html",
    "styles.css": "css",
    "file.txt": "txt"
}

# Code snippets (no emojis)
code_snippets = {
    "js": [
        'const greetUser = (name) => `Hello, ${name}!`;',
        'function isEven(num) {\n    return num % 2 === 0;\n}',
        'class User {\n    constructor(name, email) {\n        this.name = name;\n        this.email = email;\n    }\n    login() {\n        console.log(`${this.name} logged in`);\n    }\n}',
        'const tasks = [\'Buy milk\', \'Call John\', \'Fix bug #22\'];\ntasks.forEach((task, i) => console.log(`${i + 1}. ${task}`));',
        'async function getData(url) {\n    try {\n        const res = await fetch(url);\n        const data = await res.json();\n        console.log(data);\n    } catch (err) {\n        console.error("Error:", err);\n    }\n}'
    ],
    "html": [
        '<h1>Hello World</h1>',
        '<p>This is a sample paragraph.</p>',
        '<input type="text" placeholder="Username">',
        '<script src="script.js"></script>'
    ],
    "css": [
        'body { font-family: Arial; background: #f0f0f0; }',
        'h1 { color: #333; }',
        '.btn { background: blue; color: white; }'
    ],
    "txt": [
        "Project notes:\n- Improve layout\n- Add dark mode\n- Test login page",
        "Today's goals:\n- Refactor script.js\n- Write styles for form",
        "Client feedback:\n- 'Make the site mobile-friendly'\n- 'Too many popups'"
    ]
}

def write_to_file(file_name, content_type):
    snippet = random.choice(code_snippets[content_type])
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(snippet + "\n")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Wrote to {file_name}:\n{snippet.splitlines()[0]}...")

# Break settings
session_start = datetime.now()
break_every = timedelta(minutes=30)
break_length = timedelta(minutes=5)
next_break = session_start + break_every

# Weighted file priority
weighted_files = (
    ["script.js"] * 4 +
    ["logic.js"] * 3 +
    ["app.js"] * 3 +
    ["index.html"] +
    ["styles.css"] +
    ["file.txt"]
)

# Main loop
while True:
    now = datetime.now()

    if now >= next_break:
        print(f"\n[BREAK] Taking a 5-minute break at {now.strftime('%H:%M:%S')}\n")
        time.sleep(break_length.total_seconds())
        next_break = datetime.now() + break_every
        continue

    file = random.choice(weighted_files)
    file_type = files[file]
    write_to_file(file, file_type)

    time.sleep(random.uniform(60, 80))
