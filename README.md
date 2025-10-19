# 🐱 FastAPI Cat Facts API

This is a simple FastAPI application that fetches random cat facts from the [CatFact API](https://catfact.ninja/fact) and returns user information, a timestamp, and a random cat fact.

---

## 📦 GitHub Repository
🔗 [https://github.com/sneekywhite/HngInfoProject.git]

---

## 🚀 Features
- Fetches a random cat fact from an external API  
- Returns:
  - API status (`Success` or `Failed`)
  - User info (email, name, stack)
  - Current UTC timestamp (ISO 8601 format)
- Handles network or API errors gracefully

---

## 🧠 Tech Stack
- **Language:** Python 3.9+
- **Framework:** FastAPI
- **Server:** Uvicorn
- **HTTP Client:** Requests

---

## 🧩 Dependencies
| Package | Description |
|----------|--------------|
| `fastapi` | Framework for building APIs quickly |
| `uvicorn` | ASGI server to run FastAPI |
| `requests` | For fetching external API data |

---

## ⚙️ Installation & Setup Instructions

### 1️⃣ Clone the repository
```bash
git https://github.com/sneekywhite/HngInfoProject.git
cd HNG_API_PROJECT
python -m venv env
source env/bin/activate     # On macOS/Linux
env\Scripts\activate        # On Windows
pip install -r requirements.txt
pip freeze > requirements.txt # If requirement bis empty , regenerate
uvicorn main:app --reload


