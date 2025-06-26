# Masab Farooque's AI Portfolio Support Agent

Welcome to the official repository for **Masab's AI Portfolio Support Agent**! This project demonstrates a professional AI-powered support agent that answers questions about Masab Farooque's skills, experience, and professional background.

---

## 🚀 Project Overview

This repository contains a full-stack application with a FastAPI backend and a simple frontend. The backend leverages advanced AI (via LangChain and Groq) to provide accurate, context-aware answers about Masab Farooque, strictly based on a provided professional profile.

---

## 📁 Project Structure

```
AI Agent Supportbot/
├── backend/
│   ├── agent_core.py         # Core AI logic and session management
│   ├── main.py               # FastAPI app and API endpoints
│   ├── requirements.txt      # Python dependencies
│   ├── knowledge_base.txt    # Masab's professional profile (context)
│   └── ...
├── frontend/
│   ├── index.html            # Simple web UI
│   └── style.css             # UI styling
└── .gitignore                # Git ignore rules
```

---

## 🧠 How It Works

- **Knowledge Base:** All answers are strictly based on the content of `knowledge_base.txt` (Masab Farooque's professional profile).
- **No Hallucination:** The AI will never invent or assume information not present in the profile.
- **Session Support:** Maintains chat history for each session.
- **Professional Tone:** Always responds in a professional, helpful manner as "Masab's AI Portfolio Assistant."

---

## 🛠️ Setup & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Masab12/AI-Agent-Supportbot.git
   cd AI-Agent-Supportbot
   ```
2. **Backend Setup:**
   - Navigate to the backend folder:
     ```bash
     cd backend
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file and add your Groq API key:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Start the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```
3. **Frontend:**
   - Open `frontend/index.html` in your browser.

---

## 📦 Dependencies
- Python 3.8+
- FastAPI
- Uvicorn
- python-dotenv
- LangChain (core, groq, community)

---

## 🤖 API Endpoints
- `POST /chat` — Send a message and receive an AI response about Masab Farooque.
- `GET /` — Health/status check.

---

## 🔒 Security & Best Practices
- `.env` and other sensitive files are gitignored.
- Only `requirements.txt` is tracked (not `requirements.text`).
- The AI will never answer questions outside the provided profile context.

---

## 👤 Author
**Created by Masab Farooque**

- [GitHub](https://github.com/Masab12)
- [LinkedIn](https://www.linkedin.com/in/masabfarooque/)

---

## 📄 License
This project is for portfolio and demonstration purposes by Masab Farooque.
