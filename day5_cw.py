def main():
    moreStudent = 'y'
    students = []
    while moreStudent.lower().strip() == 'y':
        name = getName()
        gender = getGender()
        age = getAge()
        moreStudent = input(
            "\n\nDo you want add more students if yes then press 'y' else press any key: ")

        students.append(getStudent(name, gender, age))

    genderCount = operation(students)
    print("\n\n\n--------------------------------------------------------------------")

    print(
        f"Total Students: {len(students)} | Total Male: {genderCount[0]} | Total Female: {genderCount[1]}\n")

    printStudents(students)


def getName():
    name = input("Enter your name: ")
    if name.strip():
        return name.strip()
    else:
        return "no name"


def getGender():
    gender = input("Enter Gender, it should be Male / Female: ")

    if gender.strip().lower() == 'male' or gender.strip().lower() == 'female':
        return gender.strip()
    else:
        return getGender()


def getAge():
    age = input("Enter age, it should be greater than 0: ")

    if age.strip():
        try:
            age = int(age.strip())
            if age > 0:
                return age
            else:
                return getAge()
        except:
            return getAge()
    else:
        return getAge()


def getStudent(name="no name", gender="male", age=1):
    student = {"name": name, "gender": gender, "age": age}
    student["age_group"] = calculateAgeGroup(student["age"])
    return student


def operation(stduents):
    maleCount = 0
    femaleCount = 0
    for std in stduents:
        if std["gender"].lower() == "male":
            maleCount += 1
        elif std["gender"].lower() == "female":
            femaleCount += 1

        
    return (maleCount, femaleCount)


def calculateAgeGroup(age):
    if age < 12:
        return "Child"
    elif age < 18:
        return "Teenage"
    else:
        return "Adult"


def printStudents(students):
    print(f"{'S.No':<5} | {'Name':<15} | {'Gender':<8} | {'Age':<5} | Age Group")
    count = 0
    for std in students:
        count += 1

        print(
            f"{count:<5} | {std['name']:<15} | {std['gender']:<8} | {std['age']:<5} | {std['age_group']}")

    print("\n--------------------------------------------------------------------")


main()
