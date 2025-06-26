# 🤖 Calendar Booking Assistant

This is a conversational AI assistant that helps users seamlessly check availability and book appointments directly into their Google Calendar using natural language. Built using FastAPI, LangGraph, and Streamlit.

---

## 📌 Features

* 🗣 Accepts natural language queries like:

  * "Book a call on 27th June at 5 PM"
  * "Am I free this Friday at 2 PM?"
* 🗕 Integrates with Google Calendar
* ✅ Automatically checks availability and schedules meetings
* ⏱ Applies timezone handling (IST)
* 🧠 Detects intent (booking or availability)

---

## ⚙️ Tech Stack

| Layer    | Tech                |
| -------- | ------------------- |
| Backend  | FastAPI             |
| Agent    | LangGraph           |
| Frontend | Streamlit           |
| Calendar | Google Calendar API |

---

## 🧾 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/rishivejani15/AI-Calendar-Booking-Assistant.git
cd AI-Calendar-Booking-Assistant
```

### 2. Create `.env` for Google API credentials

```env
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
CALENDAR_ID=primary
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI backend

```bash
uvicorn backend.main:app --reload
```

### 5. Run Streamlit frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## 📂 Project Structure

```
calendar-booking-assistant/
├── agent/
│   ├── langgraph_agent.py
│   └── nlp_utils.py
├── backend/
│   ├── calendar_utils.py
│   └── main.py
├── frontend/
│   └── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Example Prompts to Try

* "Book a meeting on July 1st at 10 AM"
* "Am I free tomorrow at 3 PM?"
* "Schedule an appointment for next Monday"

---

## 📜 License

This project is under the MIT License.

---

## 🙌 Contributing

Feel free to fork, raise issues, or submit PRs!

---

## 👨‍💻 Built with ❤️ by Rishi Dhanesh Vejani
