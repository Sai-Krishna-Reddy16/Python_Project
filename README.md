# 🎙 Jarvis – AI Voice Assistant (Python)

This is my AI voice assistant project built using Python.  
I built it a few months ago and recently updated it to use the Gemini Flash model.

---

## 🚀 What It Can Do

- 🎤 Listen to my voice
- 🔑 Activate when I say **"Jarvis"**
- 🌐 Open Google, YouTube, Facebook, LinkedIn
- 🎵 Play songs from my custom playlist
- 📰 Tell the latest news (India)
- 🤖 Answer general questions using Gemini AI
- 🔊 Speak responses using text-to-speech

---

## 🛠 Tech Used

- Python
- SpeechRecognition
- pyttsx3
- Requests
- Gemini Flash API
- News API

---

## ▶️ How to Run

### 1️⃣ Install Requirements

```bash
pip install -r requirements.txt

```

##  2️⃣ Set Environment Variables

For Windows (PowerShell):

$Env:GEMINI_API_KEY="your_api_key"
$Env:NEWS_API_KEY="your_news_api_key"


For Command Prompt:

set GEMINI_API_KEY=your_api_key
set NEWS_API_KEY=your_news_api_key

##  3️⃣ Run the Project
```bash
python main.py
```

Then say "Jarvis" to activate.
