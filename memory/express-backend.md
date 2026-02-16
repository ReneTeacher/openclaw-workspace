# 2026-02-13 - Express Backend Created

## New Repository

**Repo**: `ReneTeacher/exam-system-backend` (Private)

## What's Created

### Express.js Backend

| File | Description |
|------|-------------|
| `src/index.js` | Main entry point |
| `src/routes/auth.js` | Register/Login/JWT |
| `src/routes/exams.js` | Exam CRUD |
| `src/routes/questions.js` | Question management |
| `src/routes/submissions.js` | Submit & Score |
| `src/middleware/auth.js` | JWT authentication |
| `src/models/database.js` | PostgreSQL connection |
| `schema.sql` | Database schema |

### API Endpoints

**Auth**:
- POST `/api/auth/register`
- POST `/api/auth/login`
- GET `/api/auth/me`

**Exams**:
- GET `/api/exams` (published)
- GET `/api/exams/teacher`
- POST `/api/exams` (teacher)
- PUT `/api/exams/:id` (teacher)
- DELETE `/api/exams/:id` (teacher)

**Questions**:
- POST `/api/questions/exam/:examId` (teacher)
- PUT `/api/questions/:id` (teacher)
- DELETE `/api/questions/:id` (teacher)

**Submissions**:
- POST `/api/submissions` (submit exam)
- GET `/api/submissions/my`
- GET `/api/submissions/exam/:examId` (teacher)

## Next Steps

### 1. Deploy PostgreSQL on Zeabur
1. Go to Zeabur dashboard
2. Add Service → PostgreSQL
3. Wait for deployment

### 2. Run Database Schema
1. Copy `schema.sql` content
2. Paste to PostgreSQL SQL Editor
3. Run

### 3. Deploy Backend
1. Go to Zeabur dashboard
2. Add Service → GitHub → Select `exam-system-backend`
3. Add environment variables:
   - `DB_HOST` (from PostgreSQL)
   - `DB_PORT` (5432)
   - `DB_NAME` (from PostgreSQL)
   - `DB_USER` (from PostgreSQL)
   - `DB_PASSWORD` (from PostgreSQL)
   - `JWT_SECRET` (your secret)
4. Deploy

## Architecture

```
┌─────────────────────────────────────┐
│         Zeabur Project               │
│                                     │
│  ┌─────────────────┐  ┌─────────┐ │
│  │ Express Backend │◄─│ Postgres │ │
│  │ (Port 3000)     │  │ Database│ │
│  └─────────────────┘  └─────────┘ │
│                                     │
└─────────────────────────────────────┘
```

## What's Left

- [ ] Deploy PostgreSQL on Zeabur
- [ ] Run schema.sql
- [ ] Deploy backend
- [ ] Create frontend (React/Vue)
