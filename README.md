# AI Code Review Platform

An AI-powered backend application that analyzes source code and provides automated review suggestions using Google's Gemini API.

<<<<<<< HEAD
## Features

- AI-powered code review
- Bug detection
- Code quality suggestions
- Time complexity analysis
- Space complexity analysis
- REST APIs using FastAPI
- Interactive API documentation with Swagger UI
=======
---

## Features

- AI-powered code review
- Code quality suggestions
- Time complexity analysis
- Space complexity analysis
- REST API using FastAPI
- Interactive API documentation using Swagger
- Environment variable support
- Modular backend architecture

---
>>>>>>> 36543211a3e2b3832cd6bdbaf21bd34dcf12aaa7

## Tech Stack

- Python
- FastAPI
- Gemini API
- Pydantic
- Uvicorn
<<<<<<< HEAD
- python-dotenv

## Project Structure

```
ai-code-review-platform/
│
├── backend/
├── frontend/
├── docs/
├── screenshots/
└── README.md
```

## Running the Project

```bash
pip install -r requirements.txt

uvicorn main:app --reload
```

## Current Status

- ✅ FastAPI backend completed
- ✅ REST API completed
- ✅ Swagger documentation completed
- ✅ Gemini API integration completed
- 🔄 Authentication in progress
- 🔄 Dashboard in progress
=======
- Python-dotenv

---

## Project Structure

backend/
│
├── app/
│ ├── routes/
│ ├── services/
│ ├── models/
│ └── utils/
│
├── main.py
├── requirements.txt
└── .env

---

## API Endpoints

GET /

Returns server status.

POST /review

Accepts source code and returns an AI-generated review.

---

## Example Request

```json
{
    "code":"for i in range(10): print(i)"
}
```

---

## Current Status

Backend is implemented with FastAPI and Gemini API integration.

Currently enhancing AI workflow and improving production readiness.

---
>>>>>>> 36543211a3e2b3832cd6bdbaf21bd34dcf12aaa7

## Future Improvements



- JWT Authentication
- Review History
- PDF Export
- User Dashboard
- React Frontend
- Docker Deployment

## Author

**Ruthwik Pamidimarri**

- GitHub: https://github.com/Ruthwik-09
- LinkedIn: https://www.linkedin.com/in/ruthwik-pamidimarri-2679b6340/
=======

>>>>>>> 36543211a3e2b3832cd6bdbaf21bd34dcf12aaa7
