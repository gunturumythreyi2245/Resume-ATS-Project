# 🤖 Resume ATS Analyzer

An AI-powered Resume Applicant Tracking System (ATS) Analyzer that evaluates resumes, compares them with job descriptions, identifies relevant and missing skills, checks important resume sections, calculates ATS scores, and generates downloadable ATS reports.

## 🚀 Overview

Many companies use Applicant Tracking Systems (ATS) to filter resumes before they reach recruiters. A resume can be technically strong but still perform poorly if it lacks relevant keywords, skills, or important sections.

This project provides a web-based platform that helps job seekers understand how well their resume matches a target job and what they can improve.

The application allows users to:

- Upload their resume
- Extract and analyze resume content
- Calculate an ATS score
- Detect important resume sections
- Identify skills present in the resume
- Compare resume skills with a Job Description
- Identify matched and missing skills
- Generate personalized suggestions
- Download an ATS analysis report
- View previous resume analysis results

---

## ✨ Features

### 📄 Resume Analysis

- Upload resumes for automated analysis
- Extract text from resume documents
- Detect important resume sections
- Extract email and phone number
- Identify technical and professional skills

### 📊 ATS Score

The system generates an ATS compatibility score based on factors such as:

- Resume sections
- Skills detected
- Resume completeness
- Relevant keywords

### 💼 Job Description Matching

Users can provide a Job Description to compare it with their resume.

The system identifies:

- ✅ Matched skills
- ❌ Missing skills
- 📊 Job Match Score

This helps users understand how closely their resume aligns with a specific job opportunity.

### 💡 Resume Improvement Suggestions

The application provides suggestions based on detected weaknesses in the resume, helping users improve its ATS compatibility and completeness.

### 📑 ATS Report Generation

Users can generate and download a structured PDF report containing:

- ATS Score
- Contact information
- Skills found
- Matched skills
- Missing skills
- Resume section analysis
- Improvement suggestions

### 🔐 User Authentication

The application includes:

- User registration
- Login
- Logout
- Session management
- User-specific analysis history

### 📚 Analysis History

Previously analyzed resumes can be stored and accessed through the user's history.

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Backend

- Python
- Flask

### Resume Processing

- PyPDF2
- python-docx

### Data & Storage

- SQLite
- Python

### Report Generation

- ReportLab

### Deployment

- Gunicorn

### Version Control

- Git
- GitHub

---

## 🏗️ Project Structure

```text
Resume-ATS-Project/
│
├── static/
│   ├── css/
│   └── uploads/
│
├── templates/
│   ├── dashboard.html
│   ├── history.html
│   ├── index.html
│   ├── login.html
│   ├── result.html
│   └── signup.html
│
├── utils/
│   ├── ats_score.py
│   ├── database.py
│   ├── job_match.py
│   ├── matcher.py
│   ├── parser.py
│   ├── reports.py
│   ├── sections.py
│   ├── skills.py
│   └── suggestions.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
