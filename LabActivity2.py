def check_fast_lane(minutes_left, items, teacher_pass):
    if teacher_pass:
        return "Fast lane approved"
    
    if minutes_left < 10 and items <= 3:
        return "Fast lane approved"
    else:
        return f"Use regular line (You have {minutes_left} minutes left)"

students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]

def main():
    approved_counter = 0

    print(" Cafeteria Fast Lane Checker ")

    for student in students_in_line:
        name = student["name"]
        mins = student["minutes_left"]
        items = student["items"]
        pass_status = student["teacher_pass"]

        result = check_fast_lane(mins, items, pass_status)

        if result == "Fast lane approved":
            approved_counter += 1
            print("- {name}: Fast lane approved!")
        else:
            print(f"- {name}: {result}")

    print()
    print("Total students approved for Fast Lane: {approved_counter}")
    print("")

if __name__ == "__main__":
    main()
