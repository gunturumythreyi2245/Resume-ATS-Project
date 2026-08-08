import re
from utils.skills import SKILLS


def extract_email(text):

    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    return email[0] if email else "Not Found"


def extract_phone(text):

    phone = re.findall(r"\b\d{10}\b", text)

    return phone[0] if phone else "Not Found"


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill.lower() in text:

            found.append(skill.title())

    return sorted(list(set(found)))
def calculate_ats(resume_skills, jd_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    matched = sorted(list(resume_set.intersection(jd_set)))
    missing = sorted(list(jd_set - resume_set))

    if len(jd_set) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_set)) * 100)

    return score, matched, missing