import os
from core.matcher import match_job_description

JOB_DIR = "../data/job_descriptions"

for job_file in os.listdir(JOB_DIR):
    path = os.path.join(JOB_DIR, job_file)
    with open(path, "r") as f:
        job_desc = f.read()

    print(f"\nMatching for {job_file}:")
    results = match_job_description(job_desc)
    for res in results:
        print(f" - {res['filename']} | Score: {res['score']}")