# 🎸 The Guitar Emporium - AI Sales Assistant

A modern, AI-powered guitar store showcase app built with **FastAPI** and **Streamlit**. Ask natural language questions about guitars in stock, and get instant, visually rich answers—complete with images, specs, and more!

---

## ✨ Features
- **Conversational AI**: Ask about guitars, specs, price ranges, and more.
- **Beautiful UI**: Retro-inspired, mobile-friendly design with product cards and images.
- **Live Product Data**: Uses a mock JSON database for demo purposes.
- **OpenAI Integration**: Natural language understanding and smart responses.
- **Easy Deployment**: Ready for Render.com, Streamlit Cloud, or local use.

---

## 🛠️ Tech Stack
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI/LLM**: [Langchain](https://python.langchain.com/) + [OpenAI API](https://platform.openai.com/)
- **Data**: `mock_data.json` (sample guitar products)

---

## 🚀 Quick Start (Local)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/guitar-emporium-ai.git
   cd guitar-emporium-ai
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key:**
   - Create a `.env` file:
     ```
     OPENAI_API_KEY=sk-...
     ```
4. **Run the FastAPI backend:**
   ```bash
   uvicorn main:app --reload
   ```
5. **Run the Streamlit frontend (in a new terminal):**
   ```bash
   streamlit run app.py
   ```
6. **Open your browser:**
   - Visit [http://localhost:8501](http://localhost:8501) for the UI
   - The backend runs at [http://localhost:8000](http://localhost:8000)

---

## 🌐 Deploy for Free (Recommended: Render.com)

1. **Push your code to GitHub.**
2. **Create two Render.com Web Services:**
   - **FastAPI backend:**
     - Build: `pip install -r requirements.txt`
     - Start: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - **Streamlit frontend:**
     - Build: `pip install -r requirements.txt`
     - Start: `streamlit run app.py --server.port 10001 --server.address 0.0.0.0`
3. **Set environment variables** (like your OpenAI API key) in Render dashboard.
4. **Update `API_URL` in `app.py`** to your deployed FastAPI URL.

---

## 📁 Project Structure
```
├── app.py            # Streamlit frontend
├── main.py           # FastAPI backend
├── chat.py           # AI logic (Langchain + OpenAI)
├── data.py           # Loads product data from mock_data.json
├── mock_data.json    # Sample guitar product data
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── ...
```

---

## 📝 License
This project is for educational and showcase purposes. Feel free to fork and adapt!

---

## 🙏 Credits
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [Langchain](https://python.langchain.com/)
- [OpenAI](https://platform.openai.com/)

---

Enjoy exploring The Guitar Emporium! If you like it, ⭐️ the repo and share your feedback! 