def load_data():
    my_file = open("students.txt", 'r')
    lines = my_file.readlines()
    students_file_data = []
    for file_line in lines:
        split_file_line = file_line.split(',')
        file_line_data = {
            'name': split_file_line[0],
            'GPA': int(split_file_line[1]),
            'change': float(split_file_line[2])
        }
        students_file_data.insert(0, students_data)
    return students_file_data

def print_menu():
    print("========Please selection from the following:=======")
    print("[1] Add student")
    print("[2] Find masters students")
    print("[3] Find students on probation")
    print("[4] Find honors students")
    print("====================================================")

def find_lowest(students_file_data):
    lowest_so_far = students_file_data[0]
    for current_GPA in students_file_data:
        if current_GPA['pop'] < lowest_so_far['GPA']:
            lowest_so_far = current_GPA
    print(f"{lowest_so_far['name']} is the student with the lowest GPA {lowest_so_far['GPA']}")


def find_highest(students_file_data):
    highest_so_far = students_file_data[0]
    for current_GPA in students_file_data:
        if current_GPA['GPA'] > highest_so_far['GPA']:
            highest_so_far = current_GPA
    print(f"------------------")
    print(f"The student with the highest GPA is {highest_so_far['name']}")
    print("------------------")

def add_new_student(students_file_data):
    student_name = input("Please enter the name of the student:")
    students_GPA = int(input(f"enter student GPA {student_name}:"))
    GPA_change = float(input(f"What is {students_name}'s GPA"))
    new_student = {
        "name": students_name,
        'GPA': students_GPA,
        'change': GPA_change
    }
    students_file_data.append(new_student)
def process_user_input(user_choice, students_data):
    if user_choice == '1':
        find_lowest(students_data)
    elif user_choice == '2':
        find_highest(students_data)
    elif user_choice == '3':
        add_new_student(students_data)
    elif user_choice == '4':
        exit(0)
    else:
        print("Invalid Selection, please choose 1-4")
def main():
    student_list = load_data()
    while True:
        print_menu()
        user_selection = input("Your choice 1-4:")
        process_user_input(user_selection, student_list)

main()
