def check_borrowing(overdue_books, status):
    if overdue_books:
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    elif status == "active":
        return "Borrowing allowed"
    else:
        return "Not allowed: invalid status"

def main():
    successful_borrowers = 0

    print("=== Welcome to Aliah's Library Kiosk ===")

    while True:
        print()
        name = input("Enter student name (or type 'exit' to quit): ").strip()
        
        if name.lower() == "exit":
            break
            
        has_overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
        has_overdue = has_overdue_input == "yes"

        status = input("Enter your status (active/suspended): ").strip().lower()
        
        try:
            books_requested = int(input("How many books do you want to borrow? "))
        except ValueError:
            print("Invalid input! Please enter a valid number of books next time.")
            continue
            
        result = check_borrowing(has_overdue, status)

        if result == "Borrowing allowed":
            if books_requested <= 0:
                print("Notice: You requested 0 or negative books. No borrowing was processed.")
            elif books_requested > 3:
                print("Warning: You can only borrow a maximum of 3 books at a time.")
              
                print("Success:", name, "is allowed to borrow 3 books.")
                successful_borrowers += 1
            else:
              
                print("Success:", name, "is allowed to borrow", books_requested, "book(s).")
                successful_borrowers += 1
        else:
            print("Result for", name + ":", result)

    print()
    print("Kiosk Session Ended.")
    print("Total students successfully allowed to borrow:", successful_borrowers)

if __name__ == "__main__":
    main()
