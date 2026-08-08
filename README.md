# Resume ATS Analyzer

An AI-powered Resume Applicant Tracking System (ATS) Analyzer built with Python and Flask. The application analyzes resumes against job descriptions, calculates an ATS compatibility score, identifies matched and missing skills, evaluates resume sections, and provides personalized improvement suggestions.

## 🚀 Features

- 📄 Resume PDF upload and parsing
- 🤖 ATS-based resume analysis
- 📊 ATS compatibility score
- 🎯 Job description and resume matching
- ✅ Matched skills identification
- ❌ Missing skills identification
- 📝 Resume section analysis
- 💡 Personalized resume improvement suggestions
- 📑 Downloadable ATS analysis reports
- 👤 User signup and login
- 🔐 Password-protected user accounts
- 🗃️ SQLite database for user and analysis data
- 📚 Analysis history
- 🌐 Flask-based web interface
- 📱 Responsive HTML/CSS interface

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- SQLite

### Resume Processing & NLP
- PyPDF2
- pdfplumber
- spaCy
- NLTK

### Frontend
- HTML5
- CSS3
- JavaScript

### Other Tools
- ReportLab
- python-docx
- Gunicorn
- Git & GitHub

## ⚙️ How It Works

1. User creates an account or logs in.
2. User uploads their resume in PDF format.
3. User provides a target job description.
4. The system extracts text from the resume.
5. Resume sections and skills are identified.
6. Resume content is compared with the job description.
7. The system calculates an ATS compatibility score.
8. Matched and missing skills are displayed.
9. Personalized improvement suggestions are generated.
10. The analysis can be saved to history and downloaded as a report.

## 📂 Project Structure

```text
Resume-ATS-Project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── result.html
│   └── history.html
│
├── static/
│   ├── css/
│   └── uploads/
│
└── utils/
    ├── ats_score.py
    ├── database.py
    ├── job_match.py
    ├── matcher.py
    ├── parser.py
    ├── reports.py
    ├── sections.py
    ├── skills.py
    └── suggestions.py
