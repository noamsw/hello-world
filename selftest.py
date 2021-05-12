def checkId(student):
        id = student[0].strip()
        if id[0] == '-' or int(id[0]) == 0:
            return False
        id = int(float(student[0].strip()))
        if id > 99999999 or id < 10000000:
            return False          
        student[0] = id
        return True

def checkname(student):
        is_letters = True
        for letter in student[1].strip(' '):
            if ((ord(letter) < ord('a') or ord(letter) > ord('z')) 
                and (ord(letter) < ord('A') or ord(letter) > ord('Z')) 
                and (letter != ' ')):
                is_letters = False
                break
        return is_letters


def checkageAndYear(student):
        age = int(student[2].strip())
        if age > 120 or age <16:
            return False
        if int(student[3].strip()) != 2020 - age:
            return False
        student[2] = age
        student[3] = int(student[3].strip(' '))
        return True
        
    
def checksemestert(student):
        if int(student[4].strip()) < 1:
            return False
        student[-1] = int(student[-1].strip(' \n'))
        return True

def checkStudent(student):
    if not(checkId(student)):
        return False
    if not(checkname(student)):
        return False
    if not(checkageAndYear(student)):
        return False
    if not(checksemestert(student)):
        return False
    return True

def correctAgeAvg(in_file_path: str, semester: int):
    if semester < 1:
        return -1
    f = open(in_file_path, 'r')
    lst = []
    good_dict = {}
    sum_age = 0.0
    sum_students = 0
    for line in f:
        lst.append(line.split(','))
    for student in lst:
        if not(checkStudent(student)):
            continue
        good_dict[student[0]] = (student[1],student[2],student[3],student[4])
    for id in good_dict:
        if good_dict[id][3] == semester:
            sum_age += int(good_dict[id][1])
            sum_students += 1
    f.close()
    if sum_students == 0:
        return 0
    return (sum_age/sum_students)

print(correctAgeAvg("/home/noamwolf/testxt.txt", 3))