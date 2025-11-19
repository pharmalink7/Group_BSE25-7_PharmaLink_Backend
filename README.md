PharmaLink – Backend API

This repository contains the backend API for PharmaLink, a modern platform designed to help users check medicine prices and availability across pharmacies in Uganda. The backend is developed using Django and Django REST Framework, and serves a React frontend and future Flutter mobile application.

1. Overview

PharmaLink provides the following capabilities:

Patients can search for medicines and compare prices across pharmacies.

Pharmacies can manage medicines, prices, and stock through a secure dashboard.

The system includes admin-controlled access, ensuring only verified pharmacies are added.

An AI-powered symptom checker is being integrated to suggest safe over-the-counter medicines.

Important Access Note
User and pharmacy registration is restricted.
Only administrators can add pharmacies and user accounts through the Django Admin Panel to ensure controlled access.

2. Technology Stack
Layer	Technology
Backend	Django 5, Django REST Framework
Authentication	JWT (SimpleJWT)
Database	SQLite (development), PostgreSQL (production via Render)
Frontend	React
Deployment	Render (Backend), CI/CD Pipeline
3. Project Structure
```
Group_BSE25-7_PharmaLink_Backend/
│
├── apps/
│ ├── users/ # Handles user authentication and management
│ └── pharmacies/ # Manages pharmacy profiles and medicine inventory
│
├── pharmacy_project/ # Main Django project configuration
├── manage.py # Django's command-line utility for administrative tasks
├── requirements.txt # A list of Python dependencies for the project
└── README.md # This file
```
5. Authentication

The API uses JWT Authentication.

How it works:

Admin creates a user account.

User logs in to obtain access and refresh tokens.

Tokens are included in Authorization headers for protected endpoints.

Header Format

Authorization: Bearer <access_token>

5. Base URL

Production (Render):
```
https://pharmalink-x7j6.onrender.com/api/
```

All endpoints listed below are relative to this base URL.

6. API Endpoints
6.1 User Login (Token Generation)
POST /api/token/


Request:
```
{
  "email": "user@example.com",
  "password": "password123"
}
```


Response:
```
{
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}
```
6.2 Pharmacy Endpoints
Get all pharmacies
GET /api/pharmacies/


Response:
```
[
  { "id": 1, "name": "City Health Pharmacy", "address": "Main Street" },
  { "id": 2, "name": "Kampala Central Pharmacy", "address": "Market Road" }
]
```
6.3 Medicine Endpoints
Get all medicines
GET /api/medicines/


Public access. Returns medicines from all pharmacies.

Create a new medicine
POST /api/medicines/


Authentication required.

Request:
```
{
  "name": "Ibuprofen 200 mg",
  "description": "Pain reliever and anti-inflammatory",
  "price": "9.99"
}
```

Response:
```
{
  "id": 1,
  "name": "Ibuprofen 200 mg",
  "description": "Pain reliever and anti-inflammatory",
  "price": "9.99"
}
```
Get medicines for logged-in pharmacy
GET /api/medicines/my_medicines/


Response:
```
[
  {
    "id": 1,
    "name": "Paracetamol",
    "description": "Pain relief and fever reduction",
    "price": "5.00"
  }
]
```
6.4 AI Symptom Checker (Upcoming)
POST /api/symptom-checker/


Request:
```
{
  "symptoms": "Headache and slight fever"
}
```

Response:
```
{
  "suggested_condition": "Mild fever and headache",
  "suggested_medicines": ["Acetaminophen", "Ibuprofen"],
  "advice": "Follow dosage instructions and seek care if symptoms worsen."
}
```
7. Installation Guide (Developer Setup)

Follow the steps below to run the backend locally.

Step 1 — Clone the Repository
```
git clone https://github.com/ndjek1/Group_BSE25-7_PharmaLink_Backend.git
```
```
cd Group_BSE25-7_PharmaLink_Backend
```

Step 2 — Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

Step 3 — Install Dependencies
```
pip install -r requirements.txt
```

Step 4 — Apply Database Migrations
```
python manage.py migrate
```

Step 5 — Start the Development Server
```
python manage.py runserver
```


Backend will be available at:
http://127.0.0.1:8000/api/

8. User Manual
Admin (Backend Panel)

Access:
```
http://127.0.0.1:8000/admin/
```

Admin Capabilities:

Add pharmacies

Create and manage user accounts

View and edit medicines

Manage permissions

Pharmacy User

After admin account creation:

Log in via frontend.

Access pharmacy dashboard.

Add, update, or delete medicines.

Manage price and stock information.

Patient User (Public Access)

Search for medicines

Compare prices across pharmacies

Use AI symptom checker (upcoming)

9. Running Tests

Run backend tests:

python manage.py test

10. Contributors
Name	Role
Ndjekornom Victoire	Backend Lead
Alvin	CI/CD & Deployment
Lasse	Project Documentation
Cyiza	Frontend Integration
Yusuf	Testing & Documentation
11. Conclusion

PharmaLink provides a reliable, efficient, and scalable platform for pharmacy price comparison and medicine availability. The system ensures controlled access through admin-managed accounts, and continues to integrate AI capabilities for enhanced user experience.
