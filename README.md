 PharmaLink – Pharmacy Price & Availability Checker API

This is the backend API for the PharmaLink project — a modern, AI-ready platform for checking medicine prices and availability across pharmacies in Uganda.
It is built using Django + Django REST Framework, and serves a React frontend.

🚀 Overview

PharmaLink allows:

🧍‍♂️ Patients to search medicines and compare prices

💊 Pharmacies to manage their inventory and pricing

🧠 (Upcoming) AI Symptom Checker that suggests safe over-the-counter medicines

🛠️ Admin to manage users and pharmacies through the backend dashboard

🧩 Note:
Registration for users and pharmacies is restricted.
Only admins can add new pharmacies and user accounts through the Django Admin Panel.
This ensures verified pharmacies and controlled system access.

🧠 (Upcoming) AI Symptom Checker that suggests possible medicines based on user-entered symptoms.

⚙️ Tech Stack
Layer	Technology
Backend	Django 5, Django REST Framework
Auth	JWT (via SimpleJWT)
Database	SQLite (development) / PostgreSQL (production)
Frontend	React (consumes these APIs)
Deployment	Render (CI/CD with GitHub Actions)

📁 Project Structure

Group_BSE25-7_PharmaLink_Backend/
│
├── apps/
│   ├── users/              # Custom User model linked to Pharmacy
│   └── pharmacies/         # Pharmacies and Medicines management
│
├── pharmacy_project/       # Main Django project
├── manage.py
├── requirements.txt
└── README.md

🔐 Authentication Flow

The API uses JWT (JSON Web Tokens).

Register an account

Log in to get an access and refresh token

Include the token in the Authorization header for protected requests

Header Format

Authorization: Bearer <your_access_token>

🌐 Base URL

Live API:
https://pharmalink-x7j6.onrender.com

All endpoints are relative to this base.

🧍 User Endpoints
2️⃣ Login (Get Token)

POST /api/token/

Request Body
```
{
  "email": "newuser@example.com",
  "password": "newpass123"
}
```

Response (200 OK)
```
{
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}
```
🏥 Pharmacy Endpoints
Get All Pharmacies

GET /api/pharmacies/

Response
```
[
  { "id": 1, "name": "City Health Pharmacy", "address": "123 Main St" },
  { "id": 2, "name": "Render Live Pharmacy", "address": "456 Cloud Way" }
]
```
💊 Medicine Endpoints
1️⃣ Get All Medicines

GET /api/medicines/
Authentication: None

Returns all medicines from all pharmacies.

2️⃣ Create a New Medicine

POST /api/medicines/
Authentication: Required (Bearer token)

Request
```
{
  "name": "Ibuprofen 200 mg",
  "description": "Relieves pain and reduces inflammation.",
  "price": "9.99"
}
```

Response
```
{
  "id": 1,
  "name": "Ibuprofen 200 mg",
  "description": "Relieves pain and reduces inflammation.",
  "price": "9.99"
}
```
3️⃣ Get Medicines for Logged-in Pharmacy

GET /api/medicines/my_medicines/
Authentication: Required (Bearer token)

Response
```
[
  {
    "id": 1,
    "name": "Paracetamol",
    "description": "Pain reliever and fever reducer",
    "price": "5.00"
  }
]
```
🤖 (Upcoming) AI Symptom Checker

Endpoint: /api/medicines/symptom-checker/
Users can enter their symptoms, and the AI (powered by Google Gemini) suggests safe, over-the-counter medicines and relevant advice.

Example request:
```
{ "symptoms": "I have a headache and slight fever" }
```
🧪 Continuous Integration (CI) & Code Quality

This project uses GitHub Actions for continuous integration.

CI Workflow

Triggered on every push and pull request to main

Performs:

✅ Run Django tests

🧩 Build React frontend and run frontend tests

🧹 Run linters (flake8, eslint)

Run Linters Locally

Backend

pip install flake8
flake8 . --config=.flake8


Frontend

npm install
npm run lint

🧰 Local Setup
git clone https://github.com/ndjek1/Group_BSE25-7_PharmaLink_Backend.git
cd Group_BSE25-7_PharmaLink_Backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver


Visit: http://127.0.0.1:8000/api/

📘 Testing

Run all backend tests:

python manage.py test

💡 Contributors
Name	Role
Ndjekornom Victoire	Backend Lead
Alvin	CI/CD & DevOps
Cyiza	Frontend Integration
Yusuf	Documentation & Testing
🏁 Thank you for using PharmaLink!

Smart access to reliable pharmacies — faster, safer, smarter. 💙
