import json
import os

DATA_FILE = "gradebook.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠ Error loading data: {e}")
        return []

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"⚠ Error saving data: {e}")

def add_course(data):
    code = input("Course code: ").upper()

    # Check duplicate
    for c in data:
        if c["code"] == code:
            print("⚠ Course already exists!")
            return

    # Validate non-empty name
    while True:
        name = input("Course name: ").strip()
        if name != "":
            break
        print("⚠ Name cannot be empty.")

    # Safe input for numbers
    while True:
        try:
            credits = float(input("Credits: "))
            break
        except ValueError:
            print("⚠ Please enter a valid number for credits.")
    while True:
        try:
            score = float(input("Score (0–10): "))
            if 0 <= score <= 10:
                break
            else:
                print("⚠ Score must be between 0 and 10.")
        except ValueError:
            print("⚠ Please enter a valid number for score.")

    # Validate non-empty semester
    while True:
        semester = input("Semester (e.g. 2024-1): ").strip()
        if semester != "":
            break
        print("⚠ Semester cannot be empty.")

    course = {
        "code": code,
        "name": name,
        "credits": credits,
        "semester": semester,
        "score": score
    }

    data.append(course)
    save_data(data)
    print("✔ Added successfully!")

def view_courses(data):
    if not data:
        print("No courses found.")
        return

    print("\n===== GRADEBOOK =====")
    for c in data:
        print(f"{c['code']} - {c['name']} | Credits: {c['credits']} | Score: {c['score']} | Semester: {c['semester']}")
    print("=====================\n")

def update_course(data):
    code = input("Enter course code to update: ").upper()

    for c in data:
        if c["code"] == code:
            print(f"Editing [{c['name']}]")

            while True:
                name = input("New course name: ").strip()
                if name != "":
                    c["name"] = name
                    break
                print("⚠ Name cannot be empty.")

            while True:
                try:
                    c["credits"] = float(input("New credits: "))
                    break
                except ValueError:
                    print("⚠ Please enter a valid number for credits.")

            while True:
                semester = input("New semester: ").strip()
                if semester != "":
                    c["semester"] = semester
                    break
                print("⚠ Semester cannot be empty.")

            while True:
                try:
                    score = float(input("New score (0–10): "))
                    if 0 <= score <= 10:
                        c["score"] = score
                        break
                    else:
                        print("⚠ Score must be between 0 and 10.")
                except ValueError:
                    print("⚠ Please enter a valid number for score.")

            save_data(data)
            print("✔ Updated!")
            return

    print("⚠ Course not found.")

def delete_course(data):
    code = input("Enter course code to delete: ").upper()

    for c in data:
        if c["code"] == code:
            data.remove(c)
            save_data(data)
            print("✔ Deleted!")
            return

    print("⚠ Course not found.")

def calculate_gpa(data):
    if not data:
        print("No data.")
        return

    total_score = 0
    total_credit = 0

    for c in data:
        total_score += c["score"] * c["credits"]
        total_credit += c["credits"]

    if total_credit == 0:
        print("No credits to calculate GPA.")
        return

    gpa = total_score / total_credit
    print(f"📌 Overall GPA: {round(gpa, 2)}")

    # GPA by semester
    semester_dict = {}
    for c in data:
        sem = c["semester"]
        if sem not in semester_dict:
            semester_dict[sem] = {"total_score":0, "total_credit":0}
        semester_dict[sem]["total_score"] += c["score"] * c["credits"]
        semester_dict[sem]["total_credit"] += c["credits"]

    print("\n===== GPA BY SEMESTER =====")
    for sem, info in semester_dict.items():
        gpa_sem = info["total_score"] / info["total_credit"] if info["total_credit"] != 0 else 0
        print(f"{sem}: {round(gpa_sem,2)}")
    print("============================\n")

def main():
    data = load_data()

    while True:
        print("""
===== MENU =====
1. Add course
2. Update course
3. Delete course
4. View gradebook
5. Calculate GPA
0. Exit
""")
        choice = input("Choose: ")

        if choice == "1":
            add_course(data)
        elif choice == "2":
            update_course(data)
        elif choice == "3":
            delete_course(data)
        elif choice == "4":
            view_courses(data)
        elif choice == "5":
            calculate_gpa(data)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


