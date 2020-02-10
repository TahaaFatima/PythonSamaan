def naam_mango():
    name = input('Enter your name : ')
    if name.strip():
        return name
    else:
        return "no name"

def age_mango():
    age = input('Enter your age : ')
    if age.strip():
        return age
    else:
        return "no age"

jobhi = []
addMore = 'y'
while addMore.strip().lower() == 'y':
    name = naam_mango()
    age  = age_mango()
    jobhi.append({'name' : name, 'age': age})

    addMore = input("If you want to add more name press 'y' : ")

print(jobhi)