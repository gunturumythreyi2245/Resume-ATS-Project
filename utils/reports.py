from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from xml.sax.saxutils import escape


def generate_report(
    filename,
    score,
    email,
    phone,
    skills,
    matched,
    missing,
    sections,
    suggestions,
    job_score=0,
    jd_matched=None,
    jd_missing=None
):

    # Handle empty values
    skills = skills or []
    matched = matched or []
    missing = missing or []
    sections = sections or {}
    suggestions = suggestions or []
    jd_matched = jd_matched or []
    jd_missing = jd_missing or []

    # Create PDF
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    elements = []


    # TITLE
    elements.append(
        Paragraph(
            "<b>AI Resume ATS Analysis Report</b>",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 15))


    # ATS SCORE
    elements.append(
        Paragraph(
            f"<b>ATS Score:</b> {score}%",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 10))


    # JOB MATCH SCORE
    if job_score:

        elements.append(
            Paragraph(
                f"<b>Job Description Match Score:</b> {job_score}%",
                styles["Heading2"]
            )
        )

        elements.append(Spacer(1, 10))


    # CONTACT INFORMATION
    elements.append(
        Paragraph(
            "<b>Contact Information</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Email:</b> {escape(str(email or 'Not detected'))}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Phone:</b> {escape(str(phone or 'Not detected'))}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 15))


    # SKILLS FOUND
    elements.append(
        Paragraph(
            "Skills Found",
            styles["Heading2"]
        )
    )

    if skills:

        for skill in skills:

            elements.append(
                Paragraph(
                    f"- {escape(str(skill))}",
                    styles["Normal"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No skills detected.",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))


    # MATCHED SKILLS
    elements.append(
        Paragraph(
            "Matched Skills",
            styles["Heading2"]
        )
    )

    if matched:

        for skill in matched:

            elements.append(
                Paragraph(
                    f"- {escape(str(skill))}",
                    styles["Normal"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No matched skills.",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))


    # MISSING SKILLS
    elements.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    if missing:

        for skill in missing:

            elements.append(
                Paragraph(
                    f"- {escape(str(skill))}",
                    styles["Normal"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No missing skills.",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))


    # JOB DESCRIPTION MATCHED SKILLS
    if jd_matched:

        elements.append(
            Paragraph(
                "Job Description Matched Skills",
                styles["Heading2"]
            )
        )

        for skill in jd_matched:

            elements.append(
                Paragraph(
                    f"- {escape(str(skill))}",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1, 15))


    # JOB DESCRIPTION MISSING SKILLS
    if jd_missing:

        elements.append(
            Paragraph(
                "Job Description Missing Skills",
                styles["Heading2"]
            )
        )

        for skill in jd_missing:

            elements.append(
                Paragraph(
                    f"- {escape(str(skill))}",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1, 15))


    # RESUME SECTIONS
    elements.append(
        Paragraph(
            "Resume Sections",
            styles["Heading2"]
        )
    )

    for section, status in sections.items():

        status_text = "Found" if status else "Missing"

        elements.append(
            Paragraph(
                f"<b>{escape(str(section))}:</b> {status_text}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))


    # SUGGESTIONS
    elements.append(
        Paragraph(
            "Improvement Suggestions",
            styles["Heading2"]
        )
    )

    if suggestions:

        for suggestion in suggestions:

            elements.append(
                Paragraph(
                    f"- {escape(str(suggestion))}",
                    styles["Normal"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No suggestions available.",
                styles["Normal"]
            )
        )


    # BUILD PDF
    doc.build(elements)