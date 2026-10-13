if __name__ == "__main__":
    count = 0

    max_name = ""
    max_grade = -1

    while True:
        name = input()
        if name == "END":
            break

        grade = int(input())

        if grade > max_grade:
            max_name = name
            max_grade = grade


    if max_grade == -1:
        print("ERROR: No s'ha introduit cap estudiant")
    else:
        print(f"{max_name}: {max_grade}")