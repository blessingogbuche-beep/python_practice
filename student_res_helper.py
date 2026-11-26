def calculate_average(score1,score2,score3):
    average = (score1 + score2 + score3) / 3
    return average

print(calculate_average(70,80,90))
print(calculate_average(0,0,0))
    

def result_status(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
print(result_status(49))
print(result_status(50))
print(result_status(75))

def assign_grade(average):
    if average >= 70:
        return "A"

    elif average  >= 60:
        return "B"

    elif average >= 50:
        return "C"

    elif average >= 40:
        return "D"
    
    else:
        return "F"

print(assign_grade(75))
print(assign_grade(65))
print(assign_grade(55))
print(assign_grade(45))
print(assign_grade(35))

def result_summary(name, average, grade, status):
    return f"{name} scored an average of {average}. Grade: {grade}. Status: {status}."

print(result_summary("Ada", 80.0, "A", "Pass"))

def run_test(name, s1, s2, s3):
    average = calculate_average(s1, s2, s3)
    status = result_status(average)
    grade = assign_grade(average)
    return result_summary(name, average, grade, status)
print(run_test("Ada", 70, 80, 90)) 
print()  
print(run_test("Ben", 50, 50, 50))
print()    
print(run_test("Cara", 40, 30, 20)) print(assign_grade(69), "expected: B")

print(assign_grade(70), "expected: A")
print(assign_grade(59), "expected: C")
print(assign_grade(60), "expected: B")
print(assign_grade(49), "expected: D")
print(assign_grade(50), "expected: C")
print(assign_grade(39), "expected: F")
print(assign_grade(40), "expected: D") 




    