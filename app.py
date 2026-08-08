from flask import Flask, render_template, request,session,send_file
from werkzeug.utils import secure_filename
from utils.parser import extract_pdf_text
from utils.ats_score import calculate_ats_score
from utils.sections import detect_sections
from utils.suggestions import generate_suggestions
from utils.reports import generate_report
from flask import send_file
from utils.job_match import calculate_job_match
from utils.matcher import (
    extract_email,
    extract_phone,
    extract_skills,
    calculate_ats,
)
import os
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, redirect, url_for, flash
from utils import database
app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "development-secret-key"
)
# Base project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Upload folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed file types
ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        confirm = request.form["confirm_password"]

        if password != confirm:

            flash("Passwords do not match.")

            return redirect(url_for("signup"))

        conn = sqlite3.connect("database.db")

        cursor = conn.cursor()

        hashed = generate_password_hash(password)

        try:

            cursor.execute(
                "INSERT INTO users(username,email,password) VALUES(?,?,?)",
                (username, email, hashed)
            )

            conn.commit()

        except sqlite3.IntegrityError:

            flash("Email already exists.")

            conn.close()

            return redirect(url_for("signup"))

        conn.close()

        flash("Account created successfully!")

        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user = cur.fetchone()

        conn.close()

        if user and check_password_hash(user[3], password):

            session["user"] = user[1]

            flash("Login Successful!", "success")

            return redirect(url_for("dashboard"))

        else:

            flash("Invalid Email or Password", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "success")

    return redirect(url_for("login"))
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    #Dashboard staistics
    cursor.execute("""
    SELECT
        COUNT(*) as total,
        MAX(ats_score) as highest,
        AVG(ats_score) as average
    FROM analysis_history
    WHERE username=?
    """, (session["user"],))

    stats = cursor.fetchone()
    cursor.execute("""
            SELECT
            resume_name, ats_score, matched,missing,analysis_date
            FROM analysis_history
            WHERE username = ?
            ORDER BY id ASC
        """, (session["user"],))

    analyses = cursor.fetchall()
    conn.close()

    return render_template(
        "dashboard.html",
        username=session["user"],
        stats=stats,
        analyses=analyses
)
@app.route("/")
def home():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("index.html")
@app.route("/history")
def history():

    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM analysis_history
        WHERE username=?
        ORDER BY analysis_date DESC
    """, (session["user"],))

    history = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        history=history
    )
@app.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return "No file selected."
    
    if "user" not in session:
        return redirect(url_for("login"))
    
    file = request.files["resume"]
    job_description = request.form.get("job_description", "")
    if file.filename == "":
        return "Please choose a file."

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(filepath)
        resume_text = extract_pdf_text(filepath)
        job_score = 0
        jd_matched = []
        jd_missing = []

        if job_description.strip():

            job_score, jd_matched, jd_missing = calculate_job_match(
            resume_text,
            job_description
    )
        job_description = request.form.get("job_description", "")
        print("\nJOB DESCRIPTION:")
        print(job_description)
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        skills = extract_skills(resume_text)
        print("\nRESUME SKILLS:")
        print(skills)
        jd_skills = extract_skills(job_description)
        print("\nJD SKILLS:")
        print(jd_skills)
        score, matched, missing = calculate_ats(
            skills,
            jd_skills
            )
        score = calculate_ats_score(
        resume_text,
        matched,
        len(jd_skills)
        )
        print("\nMATCHED:", matched)
        print("MISSING:", missing)
        print("SCORE:", score)
        sections = detect_sections(resume_text)
        suggestions = generate_suggestions(
        score,
        missing,
        sections
        )
        session["score"] = score
        session["email"] = email
        session["phone"] = phone
        session["skills"] = skills
        session["matched"] = matched
        session["missing"] = missing
        session["sections"] = sections
        session["suggestions"] = suggestions
        session["job_score"] = job_score
        session["jd_matched"] = jd_matched
        session["jd_missing"] = jd_missing
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO analysis_history
        (username, resume_name, ats_score, matched, missing, analysis_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
        session.get("user", "Guest"),
        filename,
        score,
        len(matched),
        len(missing),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

        return render_template(
            "result.html",
            resume_text=resume_text,
            email=email,
            phone=phone,
            skills=skills,
            score=score,
            matched=matched,
            missing=missing,
            sections=sections,
            suggestions=suggestions,
            job_score=job_score,
            jd_matched=jd_matched,
            jd_missing=jd_missing,
            job_description=job_description
    )


    return "Only PDF and DOCX files are allowed."

@app.route("/download")
def download():

    if "user" not in session:
        return redirect(url_for("login"))
    filename = "ATS_Report.pdf"
    generate_report(
        filename,
        session.get("score"),
        session.get("email"),
        session.get("phone"),
        session.get("skills"),
        session.get("matched"),
        session.get("missing"),
        session.get("sections"),
        session.get("suggestions"),
        session.get("job_score", 0),
        session.get("jd_matched", []),
        session.get("jd_missing", [])
    )

    return send_file(
        filename,
        as_attachment=True
    )
if __name__ == "__main__":
    app.run(debug=True)