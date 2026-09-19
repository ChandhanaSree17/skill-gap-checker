job_skills = input("Enter required skills (comma separated): ")
my_skills = input("Enter your skills (comma separated): ")

job_skills = [skill.strip().lower() for skill in job_skills.split(",")]
my_skills = [skill.strip().lower() for skill in my_skills.split(",")]

matching_skills = []
missing_skills = []

for skill in job_skills:
    if skill in my_skills:
        matching_skills.append(skill)
    else:
        missing_skills.append(skill)

match_percentage = (len(matching_skills) / len(job_skills)) * 100

print("\n===== SKILL GAP REPORT =====")

print("\nMatching Skills:")
for skill in matching_skills:
    print("✓", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✗", skill)

print(f"\nMatch Percentage: {match_percentage:.2f}%")

if missing_skills:
    print("\nRecommendation:")
    print("Focus on learning:", ", ".join(missing_skills))
else:
    print("\nYou have all the required skills!")