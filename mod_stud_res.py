def calculate_average(scores):
    average = sum(scores) / len(scores)
    return round(average, 1)

print(calculate_average([70,80,90]))
print(calculate_average([0, 0, 0]))
print(calculate_average([70,65,80]))
    

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

def run_test(name, scores ):
    average = calculate_average(scores)
    status = result_status(average)
    grade = assign_grade(average)
    return result_summary(name, average, grade, status)
print(run_test("Ada", [70, 80, 90]))
print()  
print(run_test("Ben", [50, 50, 50]))
print()    
print(run_test("Cara", [40, 30, 20]))

print()
print(assign_grade(69), "expected: B")
print(assign_grade(70), "expected: A")
print(assign_grade(59), "expected: C")
print(assign_grade(60), "expected: B")
print(assign_grade(49), "expected: D")
print(assign_grade(50), "expected: C")
print(assign_grade(39), "expected: F")
print(assign_grade(40), "expected: D") 

print()

students= {
"Ada":[70,80,90],
"Vick":[65,60,55],
"Ben":[50,50,50],
"Grace":[45,43,42],
"Cara":[40,30,20],
"Joy":[35,30,20],

}

for name, scores in students.items():
    
    print(run_test(name, scores))



    