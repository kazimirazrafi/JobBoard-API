# ⚡ JobBoard API

A social platform focused on professional networking, similar to LinkedIn.

---

## 🚀 Project Goal

To build a scalable, production-ready platform that mimics LinkedIn's core functionality while focusing on clean architecture and high performance.

---

## ✨ Key Features

### 🔐 Authentication & Security
- [ ] User Registration & Login
- [ ] JWT Access + Refresh Tokens
- [ ] Email Verification (Background Tasks)
- [ ] Password Reset Flow
- [ ] Role-Based Access Control (RBAC)

### 👥 User Roles
- **Admin:** User banning, job moderation.
- **Recruiter:** Company profiles, job posting, applicant tracking.
- **Applicant:** Job search, resume uploads, application history.

### 💼 Job Engine
- [ ] Create/Edit/Delete Job Postings
- [ ] Resume Upload & Management (File Handling)
- [ ] Bookmark/Save Jobs
- [ ] Application Status Tracking

### 🛠 Technical Specifications
- [ ] **Performance:** Redis Caching, Rate Limiting (SlowAPI)
- [ ] **Architecture:** Async Endpoints, API Versioning (v1/v2)
- [ ] **Reliability:** Structured Logging, Background Tasks (Celery)
- [ ] **Data:** Pagination, Advanced Filtering/Search

---

## 🚀 Quick Start

### 1. Prerequisites
* Python 3.10+
* Docker & Docker Compose (optional but recommended)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/kazimirazrafi/JobBoard-API
cd JobBoard-API

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Setup
```bash
cp .env.example .env
# Open .env and fill in your local credentials
```

### 4. Run the Application
```bash
# Local development with auto-reload
fastapi dev main.py
# Or using uvicorn
uvicorn app.main:app --reload
```
View the interactive docs at: [http://127.0.0](http://127.0.0)

---

## 🏗️ Project Structure
```text
├── app
│   ├── api
│   ├── core
│   ├── db
│   ├── middleware
│   ├── models
│   └── schemas
├── main.py
├── README.md
├── .env.example
└── requirements.txt
```
---

## 🛠 Tech Stack
*   **Framework:** FastAPI
*   **Database:** SQLModel
*   **Migrations:** Alembic
*   **Auth:** JWT
*   **Task Queue:** Redis
*   **Validation:** Pydantic

---

## 📂 Current Progress
- [x] Initial Project Architecture
- [ ] Database Integration (In Progress)
- [ ] Authentication System