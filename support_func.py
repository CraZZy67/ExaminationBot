import json


def pars_json_to_list(json_: dict):
    result_string = ""
    for k, v in json_.items():
        result_string += f"{k}. {v["full_name"]}\n--------------\n"
    return result_string


def sort(json_: dict):
    sorted_json = {}
    count = 1
    for k, v in json_.items():
        sorted_json[count] = v
        count += 1
    return sorted_json


def exam_len(type_: str):
    with open(f"{type_}.json", "r", encoding="utf-8") as file:
        json_len = len(json.loads(file.read()))

    if json_len > 0:
        return True
    elif json_len == 0:
        return False
