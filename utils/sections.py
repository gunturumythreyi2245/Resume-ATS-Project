def detect_sections(resume_text):

    text = resume_text.lower()

    sections = {
        "Education": False,
        "Experience": False,
        "Projects": False,
        "Skills": False,
        "Certifications": False,
        "Objective": False
    }

    if "education" in text:
        sections["Education"] = True

    if ("experience" in text or
        "internship" in text or
        "worked" in text):
        sections["Experience"] = True

    if "project" in text:
        sections["Projects"] = True

    if "skills" in text:
        sections["Skills"] = True

    if ("certification" in text or
        "certificate" in text):
        sections["Certifications"] = True

    if ("objective" in text or
        "summary" in text or
        "profile" in text):
        sections["Objective"] = True

    return sections