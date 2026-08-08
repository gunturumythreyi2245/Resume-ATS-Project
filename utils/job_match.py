import re


def calculate_job_match(resume_text, job_description):

    resume_words = set(
        re.findall(r"[A-Za-z0-9+#.]+", resume_text.lower())
    )

    jd_words = set(
        re.findall(r"[A-Za-z0-9+#.]+", job_description.lower())
    )

    if len(jd_words) == 0:
        return 0, [], []

    matched = sorted(resume_words & jd_words)

    missing = sorted(jd_words - resume_words)

    score = int(len(matched) / len(jd_words) * 100)

    return score, matched, missing