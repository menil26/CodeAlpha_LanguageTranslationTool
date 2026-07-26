# 🌍 AI Language Translation Tool

An AI-powered language translation application developed as part of the **CodeAlpha Artificial Intelligence Internship**. The application allows users to translate text into multiple languages instantly with a simple and user-friendly interface.

---

## 📌 Project Overview

The AI Language Translation Tool enables users to translate text between different languages using Google's translation service. It also includes useful features such as automatic language detection, translation history, downloadable translations, and text-to-speech playback.

This project was built using **Python** and **Streamlit** to provide an interactive web application without requiring complex frontend development.

---

## ✨ Features

- 🌍 Translate text into multiple languages
- 🔍 Auto Detect source language
- 🌐 Support for multiple target languages
- 📜 Translation history
- 🔊 Text-to-Speech (Listen to translated text)
- ⬇️ Download translated text as a `.txt` file
- 🖥️ Clean and user-friendly interface
- ⚠️ Error handling for invalid inputs

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.13

### Framework
- Streamlit

### AI / NLP
- Google Translator API (via Deep Translator)
- Google Text-to-Speech (gTTS)

### Python Libraries
- streamlit
- deep-translator
- gTTS

---

## 📦 Python Packages Used

```bash
pip install streamlit
pip install deep-translator
pip install gTTS
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
CodeAlpha_LanguageTranslationTool/
│
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
├── audio/
└── .gitignore
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/CodeAlpha_LanguageTranslationTool.git
```

### Move into the project folder

```bash
cd CodeAlpha_LanguageTranslationTool
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
```

### Activate the virtual environment

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 🌐 Supported Languages

- English
- Tamil
- Hindi
- French
- German
- Spanish
- Japanese
- Chinese
- Arabic

The application also supports **Auto Detect** for the source language.

---

## 🎯 Future Enhancements

- Copy translated text with one click
- Voice input using speech recognition
- Dark mode
- More language support
- Translation using Large Language Models (LLMs)
- Save translation history to a database

---

## 📚 What I Learned

During this project, I learned how to:

- Build an AI-based web application using Streamlit
- Integrate translation APIs into Python applications
- Generate speech from translated text using gTTS
- Handle user input and exceptions
- Manage session state in Streamlit
- Create an interactive and user-friendly interface

---

## 👩‍💻 Developed By

**Menil Sri**

Artificial Intelligence Intern  
CodeAlpha Internship 2026

---

## 📄 License

This project was developed for educational and internship purposes under the CodeAlpha Artificial Intelligence Internship Program.
