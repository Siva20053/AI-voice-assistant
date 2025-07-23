# 🔊 NAMI - AI Voice Assistant

NAMI is a powerful AI-based voice assistant built using Python. It can interact with users through voice commands, perform system-level tasks, respond intelligently using an ML-based intent classifier, and speak back naturally.

> Made with 💻 + 🧠 by **SivaRamaKrishna Reddy**

---

## 🚀 Features

- 🎤 Voice Input via Microphone
- 🧠 NLP Intent Classification (TF-IDF + Logistic Regression)
- 🗣️ Text-to-Speech (pyttsx3)
- 🌐 Web browsing (Google, YouTube, WhatsApp, Facebook, Instagram)
- 🔢 Opens & Closes Windows Apps (Notepad, Calculator)
- 🔋 Battery percentage announcement
- 🔊 Volume control (up, down, mute)
- 🤖 Intelligent responses (jokes, greetings, identity, emotions)
- 👊 Handles insults and sarcasm
- 📆 Personalized time/day-based greetings

---

## 📁 Project Structure

├── assistant.py # Main voice assistant script
├── model.py # Trains the intent classifier
├── intents.json # Dataset of intents and responses
├── intent_classifier.pkl # Trained ML model (generated after training)
├── label_encoder.pkl # Label encoder for intent tags (generated)


---

## ⚙️ Requirements

Install all required libraries using:

pip install -r requirements.txt

🧠 How It Works
Startup: Greets user based on time and day.

Listens via microphone using Google Speech Recognition.

Processes command using an ML model trained on intents.json.

Executes task: speaks a response, opens apps, browses web, controls system.

ML Pipeline:
Voice → Text → TF-IDF Vectorizer → Logistic Regression Model → Tag → Response → Speech

💻 Usage
Train the model (once):python model.py
Run the assistant:python assistant.py

Talk to NAMI like:
->“Open YouTube”
->“Tell me a joke”
->“How are you?”
->“What’s the battery status?”
->“Close notepad”

🧬 Sample Intents (from intents.json)
Greetings: hello, hi, hey
Jokes: make me laugh, tell me a joke
Identity: who are you?
Goodbye: bye, see you later
Emotions: thanks, you are awesome
Insults: idiot, shut up
System: open calculator, battery level, volume up

🧑‍💻 Author
SivaRamaKrishna Reddy
📅 Project born in July 2025
🧠 Assistant name: NAMI






