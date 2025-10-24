#Simple Grade Calculator
def parse_marks(input_str):
    """Convert space-separated marks into a list of numbers"""
    parts = input_str.strip().split()
    marks = []
    for p in parts:
        try:
            val = float(p)
            if val < 0 or val > 100:
                print(f"Invalid mark: {val} (must be 0–100)")
                return []
            marks.append(val)
        except ValueError:
            print(f"'{p}' is not a valid number")
            return []
    return marks

def average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def main():
    name = input("Enter student name: ")
    marks_input = input("Enter marks separated by spaces: ")
    marks = parse_marks(marks_input)
    if not marks:
        print("No valid marks entered. Try again.")
        return
    avg = average(marks)
    letter = grade(avg)
    print("Report:")
    print(f"{name} — Average: {avg:.2f} — Grade: {letter}")

if __name__ == "__main__":
    main()
