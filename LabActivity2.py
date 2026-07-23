def check_fast_lane(minutes_left, items, teacher_pass)
    if teacher_pass:
        return "Fast lane approved
    if minutes_left < 10 and items <= 3:
        return "Fast lane approved"
    else:
    
        return "Use regular line"

def main():
    print("=== Cafeteria Fast Lane Assistant ===")
    print()

    
    try:
        minutes_left = int(input("Enter minutes left before class starts: "))
        items = int(input("Enter number of items to purchase: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    pass_input = input("Do you have a teacher's pass? (yes/no): ").strip().lower()
    has_teacher_pass = pass_input == "yes"

    result = check_fast_lane(minutes_left, items, has_teacher_pass)

    print()
    if result == "Fast lane approved":
        print("Result:", result)
    else:
        print("Result:", result, "(You have", minutes_left, "minutes left and", items, "items)")

if __name__ == "__main__":
    main()
