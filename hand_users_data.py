import csv


def add_user(user_data: list):
    with open("data/users_data.csv", "r", encoding="utf-8") as file:
        len_csv = len(list(csv.reader(file, delimiter=",")))

    if len_csv == 0:
        with open("data/users_data.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows([["username", "first_name", "id"], user_data])
    else:
        if check_added(user_data[2]):
            with open("data/users_data.csv", "a", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(user_data)


def check_added(id_: int):
    with open("data/users_data.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        reader.__next__()

        for i in reader:
            if id_ == int(i[2]):
                return False

    return True
