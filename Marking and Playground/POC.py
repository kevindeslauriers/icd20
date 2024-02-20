import csv

def read_students_from_csv(filename):
    students = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            students.append(row[0])  # Assuming student names are in the first column
    return students

def record_contributions(students):
    contributions = {student: [] for student in students}
    while True:
        print("\nList of Students:")
        for i, student in enumerate(students, start=1):
            print("{}) {}".format(i, student))
        print("Enter the number of the student (1-{}) or 'end' to quit:".format(len(students)))
        student_index = input("Student number: ")
        if student_index.lower() == 'end':
            break
        try:
            student_index = int(student_index)
            if student_index < 1 or student_index > len(students):
                print("Invalid student number. Please enter a number between 1 and {} or 'end' to quit.".format(len(students)))
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and {} or 'end' to quit.".format(len(students)))
            continue
        
        student = students[student_index - 1]
        print("Enter the quality of contribution for {}: (r=red, y=yellow, g=green)".format(student))
        quality = input("Quality: ").lower()
        if quality not in ['r', 'y', 'g']:
            print("Invalid input. Please enter 'r', 'y', or 'g' for red, yellow, or green respectively.")
            continue
        contributions[student].append(quality)
    return contributions

def calculate_total_score(contributions):
    score_mapping = {'r': 1, 'y': 2, 'g': 3}
    total_scores = {}
    for student, scores in contributions.items():
        total_scores[student] = sum(score_mapping[score] for score in scores)
    return total_scores

def display_summary(total_scores, output_filename):
    print("\nSummary of Contributions:")
    print("{:<20} {:<10}".format("Student", "Total Score"))
    with open(output_filename, 'w') as output_file:
        output_file.write("Summary of Contributions:\n")
        output_file.write("{:<20} {:<10}\n".format("Student", "Total Score"))
        for student, score in total_scores.items():
            output_file.write("{:<20} {:<10}\n".format(student, score))
            print("{:<20} {:<10}".format(student, score))

def main():
    filename = input("Enter the filename of the CSV containing the list of students: ")
    output_filename = input("Enter the filename for the output summary: ")
    students = read_students_from_csv(filename)
    contributions = record_contributions(students)
    total_scores = calculate_total_score(contributions)
    display_summary(total_scores, output_filename)

if __name__ == "__main__":
    main()
