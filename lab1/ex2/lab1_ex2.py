'''
Python script to grade automatically a student quiz. A quiz consists in some
questions (the number of questions is not fixed and may be different for different
quizzes) and for each question there is one and only one good answer to choose
between some choices. The choices are tagged 'A', 'B', 'C', etc. and a student
quiz is a file containing a series of letters, one letter per line, each letter
being the student answer for a question. Providing the quiz solution in the same
format, it becomes easy to grade the student quiz by comparing the letters from
the two files (student file and solution file) and by counting the number of correct
and incorrect answers. The grade is the percentage of good answers and a student needs
to get at least 60% of good answers to pass.
The script allows the user to grade multiple student quizzes against one solution and
at the end the script saves the results in a CSV file with a content like:

Hulk,35.0
Zorro,75.0
Batman,100.0

Each line of the CSV file has the name of the student followed by a separator (a comma)
followed by the grade (a percentage, like 35.0, which means 35% of correct answers).
This is a sample log of the execution of the program which produces the previous
file (user input is in bold and underlined):

Welcome to the Quiz Grader

enter the quiz solution filepath: solution.txt

Enter the name of student you want to grade or nothing to exit: Hulk
Enter the student quiz filepath: hulk.txt
Hulk - 35.0% - fail

Enter the name of student you want to grade or nothing to exit: Zorro
Enter the student quiz filepath: zorro.txt
Zorro - 75.0% - pass

Enter the name of student you want to grade or nothing to exit: Batman
Enter the student quiz filepath: batman.txt
Batman - 100.0% - pass

Enter the name of student you want to grade or nothing to exit:
Enter the quiz result CSV filename: results

Thank you for using the Quiz Grader

The files batman.txt, hulk.txt, zorro.txt and solution.txt are provided
'''

def main():
    # Print welcome message
    print("Welcome to the Quiz Grader")
    
    # Get solution file and read answers
    print("enter the quiz solution filepath: ", end="")
    solution_filepath = input().strip()
    with open(solution_filepath, "r") as f:
        solution_answers = [line.strip() for line in f.readlines()]
    
    # Initialize first student input
    print("Enter the name of student you want to grade or nothing to exit: ", end="")
    student_name = input().strip()
    print("Enter the student quiz filepath: ", end="")
    student_quiz_filepath = input().strip()
    
    # Store results for CSV export
    results = []
    
    # Main grading loop
    while True:
        if student_name == "":
            break
            
        # Read student answers
        with open(student_quiz_filepath, "r") as f:
            student_answers = [line.strip() for line in f.readlines()]
            
        # Compare answers and calculate grade
        correct_count = 0
        for i in range(len(solution_answers)):
            if (solution_answers[i] == student_answers[i]):
                correct_count += 1
                
        total_questions = len(solution_answers)
        grade = (correct_count / total_questions) * 100
        status = "pass" if grade >= 60.0 else "fail"
        
        # Display results
        print(f"{student_name} - {grade:.1f}% - {status}\n")
        results.append((student_name, grade))
        
        # Get next student input
        print("Enter the name of student you want to grade or nothing to exit: ", end="")
        student_name = input().strip()
        if student_name == "":
            break
        print("Enter the student quiz filepath: ", end="")
        student_quiz_filepath = input().strip()
    
    # Save results to CSV file
    print("Enter the quiz result CSV filename: ", end="")
    csv_filename = input().strip()
    with open(csv_filename, "w") as f:
        for name, grade in results:
            f.write(f"{name},{grade:.1f}\n")
            
    # Print exit message
    print("\nThank you for using the Quiz Grader")

if __name__ == "__main__":
    main()