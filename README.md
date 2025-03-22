## 🚀 Live Demo

Access the deployed API here:  
👉 [https://safety-incident-api.onrender.com](https://safety-incident-api.onrender.com)

---

## 📌 Project Summary

A secure, RESTful Flask API built to log and retrieve safety incident reports. Features real-time token-based authentication, role-safe endpoints, and cloud deployment.

---

## 🔐 Features

- 🔒 JWT Authentication via `/register` and `/login`
- 📝 Protected POST endpoint (`/incidents`)
- 📂 Public GET endpoint for incident listing
- 🔐 Password hashing with `werkzeug.security`
- 🚀 Live deployment on Render (free tier)
- 📦 Built with Flask, SQLAlchemy, Flask-JWT-Extended

---

## 📬 API Endpoints

| Method | Route            | Description                         | Auth Required |
|--------|------------------|-------------------------------------|----------------|
| POST   | `/register`      | Register a new user                 | ❌ No          |
| POST   | `/login`         | Login and get a JWT token           | ❌ No          |
| POST   | `/incidents`     | Create a new incident               | ✅ Yes         |
| GET    | `/incidents`     | List all reported incidents         | ❌ No          |

---

## 🔧 Tech Stack

- Python + Flask
- SQLAlchemy + SQLite
- JWT Authentication
- CORS Enabled
- Hosted on [Render](https://render.com)

---

## 🧪 Test With Hoppscotch

Test your live API easily using [https://hoppscotch.io](https://hoppscotch.io)

Example token auth usage:
```http
Authorization: Bearer <your-jwt-token>
