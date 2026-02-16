# 2026-02-13 - Express + React Full Stack Exam System

## Repos Created

| Repo | Type | Purpose |
|------|------|---------|
| `ReneTeacher/exam-system-backend` | Private | Express.js API |
| `ReneTeacher/exam-system-frontend` | Private | React + Vite Frontend |

## Architecture

```
┌─────────────────────────────────────────────────┐
│                 User Browser                      │
│         https://exam-system.vercel.app           │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│               Vercel (Frontend)                  │
│              React + Vite App                    │
└────────────────────┬────────────────────────────┘
                     │ API Calls
                     ▼
┌─────────────────────────────────────────────────┐
│              Zeabur (Backend)                  │
│              Express.js API                    │
│              Port 3000                         │
└────────────────────┬────────────────────────────┘
                     │ SQL Queries
                     ▼
┌─────────────────────────────────────────────────┐
│           Zeabur PostgreSQL                     │
│              Database                          │
└─────────────────────────────────────────────────┘
```

## Deployment Steps

### 1. Backend (Express) → Zeabur
- Add Service → GitHub → exam-system-backend
- Add PostgreSQL to same project
- Set env vars (DB connection)
- Deploy

### 2. Frontend (React) → Vercel
- Go to vercel.com
- Import exam-system-frontend
- Set env var: `VITE_API_URL` = backend URL
- Deploy

## API Structure

### Auth
- POST /api/auth/register
- POST /api/auth/login
- GET /api/auth/me

### Exams
- GET /api/exams (published)
- GET /api/exams/teacher (teacher's exams)
- POST /api/exams (create)
- PUT /api/exams/:id
- DELETE /api/exams/:id

### Questions
- POST /api/questions/exam/:examId
- PUT /api/questions/:id
- DELETE /api/questions/:id

### Submissions
- POST /api/submissions
- GET /api/submissions/my
- GET /api/submissions/exam/:examId

## Files Created

### Backend
- src/index.js - Express entry
- src/routes/auth.js - Auth routes
- src/routes/exams.js - Exam CRUD
- src/routes/questions.js - Question management
- src/routes/submissions.js - Submission handling
- src/middleware/auth.js - JWT auth
- src/models/database.js - PostgreSQL connection
- schema.sql - Database schema

### Frontend
- src/App.jsx - Main router
- src/context/AuthContext.jsx - Auth state
- src/pages/Login.jsx - Login page
- src/pages/Register.jsx - Register page
- src/pages/Dashboard.jsx - Main dashboard
- src/pages/ExamList.jsx - Student exam list
- src/pages/TakeExam.jsx - Take exam
- src/pages/TeacherExams.jsx - Teacher exam management
- src/pages/CreateExam.jsx - Create exam
- src/pages/MySubmissions.jsx - View submissions
