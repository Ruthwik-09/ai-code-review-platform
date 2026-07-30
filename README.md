# AI Code Review Platform

An AI-powered backend application that analyzes source code and provides automated review suggestions using Google's Gemini API.

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

## Tech Stack

- Python
- FastAPI
- Gemini API
- Pydantic
- Uvicorn
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

## Future Improvements

- JWT Authentication

- Review History

- PDF Export

- User Dashboard

- React Frontend

- Docker Deployment
