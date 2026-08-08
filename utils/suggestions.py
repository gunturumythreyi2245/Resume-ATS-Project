def generate_suggestions(score, missing_skills, sections):

    suggestions = []

    if score < 60:
        suggestions.append("Your ATS score is low. Improve your resume by adding more relevant skills.")

    elif score < 80:
        suggestions.append("Good resume. Adding a few more keywords can improve your ATS score.")

    else:
        suggestions.append("Excellent ATS score. Your resume is well optimized.")

    if missing_skills:
        suggestions.append(
            "Add these missing skills: " +
            ", ".join(missing_skills)
        )

    if not sections["Experience"]:
        suggestions.append(
            "Include internship or work experience."
        )

    if not sections["Projects"]:
        suggestions.append(
            "Add at least two technical projects."
        )

    if not sections["Certifications"]:
        suggestions.append(
            "Include certifications to strengthen your resume."
        )

    if not sections["Objective"]:
        suggestions.append(
            "Add a professional career objective."
        )

    return suggestions