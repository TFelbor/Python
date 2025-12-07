def read_quiz(quizfile):
    with open(quizfile, 'r') as infile:
        return [c.strip() for c in infile]

def grade_quiz(student, solution):
    ok, ko = 0, 0
    for stu, sol in zip(student, solution):
        if stu == sol:
            ok += 1
        else:
            ko += 1
    return ok, ko

def grade_student(name, studentquiz, quizsolution):
    ok, ko = grade_quiz(studentquiz, quizsolution)
    return name, (ok * 100) / (ok + ko)

def display_result(result):
    name, score = result
    status = 'pass' if score >= 60 else 'fail'
    print(name, "-", str(round(score, 2)) + "%", "-", status)

def save_results(filepath, results):
    with open(filepath, "w") as outfile:
        for name, score in results:
            outfile.write(name + "," + str(score) + "\n")

def main():
    print("Welcome to the Quiz Grader\n")
    results = []
    solution = input("enter the quiz solution filepath: ").strip()
    solution = read_quiz(solution)
    while True:
        name = input("Enter the name of student you want to grade or nothing to exit: ").strip()
        if name == "":
            break
        student = input("Enter the student quiz filepath: ").strip()
        student = read_quiz(student)
        result = grade_student(name, student, solution)
        display_result(result)
        results.append(result)
    save_results(input("\nEnter the quiz result CSV filename: ").strip() + ".csv", results)

if __name__ == "__main__":
    main()
