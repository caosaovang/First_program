def find_student(id):
    '''help to find exactly student you want'''
    global student_List
    for i in range(0, len(student_List)):
        if student_List[i]['id'] == id:
            return [i, student_List[i]]
    return False


def import_student_infor():
    '''import student information
    Warning and reimport if the ID is duplicated'''
    global student_List
    infor = {'id' : '','name': ''}
    id = input("Import the student id: ")
    id = int(id)
    while True:
        student = find_student(id)
        if student != False:
            print("The ID is already existed. Please try another ID: ")
            id = input()
        else:
            break
    infor['id'] = id
    print("Import name student: ")
    infor['name'] = input()
    student_List.append(infor)

def edit_student_infor():
    '''enter the ID student 
    and then change the student name'''
    global student_List
    print("Enter the id student which you want to change: ")
    id = input()
    student = find_student(id)
    print(student[1])
    if (student != False):
        print("Enter student name: ")
        name = input()
        student[1]['name'] = name
        student_List[student[0]] = student[1]
        print(student[2])
        print(student[3])
    else:
        print("ID can not found. Please try again!")
        id = input("Enter id: ")
        id = int(id)

def delete_student():
    '''find the id student and delete student information'''
    print("Enter the student id which you want to delete: ")
    global student_List
    id = input()
    student = find_student(id)
    if (student == False):
        print("ID can not found. Please try again!")
    else:
        student_List.remove(student[1])
        print("Data has been deleted successfully.")

def show_student_data():
    '''show all the information inside student list'''
    global student_List
    for i in range(0, len(student_List)):
        print("[",student_List[i]['id'],"]", "[",student_List[i]['name'],"]")

#Main code:
student_List = []
action = 0
while (action >= 0):
    print("Enter 1 if you want to import student")
    print("Enter 2 if you want to edit student infor")
    print("Enter 3 if you want to delete student")
    print("Enter 4 if you want to show all students data")
    print("Enter 0 to get out")
    action = int(input())
    if (action == 1):
        import_student_infor()
    elif (action == 2):
        edit_student_infor()
    elif (action == 3):
        delete_student()
    elif (action == 4):
        show_student_data()
    elif (action == 0):
        break




    


