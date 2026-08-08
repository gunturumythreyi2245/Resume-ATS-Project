import re

def calculate_ats_score(resume_text, matched_skills, total_required_skills):

    score = 0

    # -----------------------
    # Contact Information (10)
    # -----------------------
    email = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    phone = re.search(r'\b\d{10}\b', resume_text)

    if email:
        score += 5

    if phone:
        score += 5

    # -----------------------
    # Education (15)
    # -----------------------

    education_keywords = [
        "education",
        "b.tech",
        "btech",
        "bachelor",
        "college",
        "university",
        "cgpa",
        "degree"
    ]

    if any(word in resume_text.lower() for word in education_keywords):
        score += 15

    # -----------------------
    # Projects (15)
    # -----------------------

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "implemented"
    ]

    if any(word in resume_text.lower() for word in project_keywords):
        score += 15

    # -----------------------
    # Experience (10)
    # -----------------------

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "worked",
        "company"
    ]

    if any(word in resume_text.lower() for word in experience_keywords):
        score += 10

    # -----------------------
    # Skills (50)
    # -----------------------

    if total_required_skills > 0:
        skill_score = (len(matched_skills) / total_required_skills) * 50
        score += skill_score

    return round(score)