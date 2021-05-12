import event_manager as EM

def fileCheck(list_out):
    for_delete = []
    for_check = 0
    for i in range(len(list_out)):
        for k in range(len(list_out[i])):
            if k == 0 and for_check == 0:
                if int(list_out[i][k]) > 99999999 or int(list_out[i][k]) < 10000000: 
                    for_delete += [i]
                    for_check = 1
            
            if k == 1 and for_check == 0:
                for j in range(len(list_out[i][k])):
                    if ord(list_out[i][k][j]) < 65 or ord(list_out[i][k][j]) > 122:
                        if for_check == 0 and list_out[i][k][j] != ' ':
                            for_delete += [i]
                            for_check = 1
                    if ord(list_out[i][k][j]) > 90 and ord(list_out[i][k][j]) < 97 and for_check == 0:
                        if list_out[i][k][j] != ' ':
                            for_delete += [i]
                            for_check = 1

            if k == 2 and for_check == 0:
                if int(list_out[i][k]) < 16 or int(list_out[i][k]) > 120:
                    for_delete += [i]
                    for_check = 1
            
            if k == 3 and for_check == 0:
                if 2020-int(list_out[i][k]) != int(list_out[i][k-1]):
                    for_delete += [i]
                    for_check = 1
            
            if k == 4 and for_check == 0:
                if int(list_out[i][k]) < 1:
                    for_delete += [i]
                    for_check = 1
        for_check = 0
        for j in range(len(list_out)):
            if for_check == 0:
                for h in range(len(for_delete)):
                    if int(list_out[i][0]) == int(list_out[for_delete[h]][0]):
                        for_check = 1
            if j == i and for_check == 0:
                break
            if int(list_out[i][0]) == int(list_out[j][0]) and for_check == 0:
                for_delete += [i]
                break
        for_check = 0
    
    for i in range(len(for_delete)):
        list_out.pop(for_delete[i] - i)


def rigtfOrder(list_out, out_file_path):
    f = open(out_file_path, 'w')
    list_in = list()
    for i in range(len(list_out)):
        list_in += [int(list_out[i][0])]
    list_in.sort()
    for i in range(len(list_in)):
        for k in range(len(list_out)):
            if int(list_out[k][0]) == list_in[i]:
                output = ", ".join(list_out[k])
                if '\n' not in output and i != len(list_in) - 1:
                    output = output + '\n'
                f.write(output)
    f.close()
                


def fileCorrect(in_file_path, out_file_path):
    list_out = list()
    f = open(in_file_path, 'r')
    for line in f:
        list_out.append(line.split(','))
    str_out = ""
    check = 0
    for i in range(len(list_out)):
        for k in range(len(list_out[i])):
            for j in range(len(list_out[i][k])):
                if list_out[i][k][j] == ' ' and k != 1:
                    continue
                if k == 1:
                    if list_out[i][k][j] != ' ':
                        check = 1
                    if check == 0:
                        continue
                    if list_out[i][k][j] == ' ' and j != len(list_out[i][k]) - 1 and j != 0:
                        if  list_out[i][k][j+1] == ' ':
                            continue
                    if j == len(list_out[i][k]) - 1 and list_out[i][k][j] == ' ':
                        continue
                
                str_out = str_out + list_out[i][k][j]
            check = 0
            list_out[i][k] = str_out
            str_out = ""
   
    fileCheck(list_out)
    rigtfOrder(list_out, out_file_path)
    f.close()


def printYoungestStudents(in_file_path, out_file_path, k):
    if k <= 0:
        return -1
    fileCorrect(in_file_path, out_file_path)
    list_out = list()
    check_min = []
    f = open(out_file_path, 'r')
    
    for line in f:
        list_out.append(line.split(', '))
    out = open(out_file_path, 'w')
    copy = k
    if k > len(list_out):
        copy = len(list_out)
    outPrint = copy
    while copy > 0:
        min = 121
        for i in range(len(list_out)):
            if int(list_out[i][2]) in check_min:
                continue
                
            if int(list_out[i][2]) < min:
                min = int(list_out[i][2])        
        check_min += [min]
        for i in range(len(list_out)):
            if int(list_out[i][2]) == min:
                
                copy = copy - 1
                if copy != 0:    
                    out.write(list_out[i][1] + '\n')
                else:
                    out.write(list_out[i][1])
            if copy == 0:
                break
    f.close()
    out.close()
    return outPrint
    
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


def getFirstDate(events):
    first_date = events[0]["date"]
    for event in events:
        if EM.dateCompare(event["date"] , first_date) < 0:
            first_date = event["date"]
    return first_date   


def printEventsList(events, file_path):
    em = EM.createEventManager(getFirstDate(events))
    for event in events:
        EM.emAddEventByDate(em, event["name"], event["date"], event["id"])
    EM.emPrintAllEvents(em, file_path)
    return em

